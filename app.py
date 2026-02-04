#!/usr/bin/env python3
"""
Web Application for Fecal Coliform Colony Counter
Upload images and get instant colony counts
"""

from flask import Flask, render_template, request, jsonify, send_file
import cv2
import numpy as np
from pathlib import Path
import os
import base64
from io import BytesIO
from PIL import Image
import json

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULTS_FOLDER'] = 'results'

# Create folders
Path(app.config['UPLOAD_FOLDER']).mkdir(exist_ok=True)
Path(app.config['RESULTS_FOLDER']).mkdir(exist_ok=True)


class ColiformCounter:
    def __init__(self, min_area=220, max_area=850, circularity_threshold=0.65):
        self.min_area = min_area
        self.max_area = max_area
        self.circularity_threshold = circularity_threshold
    
    def detect_colonies_with_color(self, image):
        """Detect colonies using both color and shape information"""
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        # Define range for blue/teal colonies
        lower_blue = np.array([80, 20, 20])
        upper_blue = np.array([140, 255, 255])
        blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
        
        # Mask for very dark objects
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, dark_mask = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY_INV)
        
        # Combine masks
        combined_mask = cv2.bitwise_or(blue_mask, dark_mask)
        
        # Clean up
        kernel = np.ones((3, 3), np.uint8)
        combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel, iterations=2)
        combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_CLOSE, kernel, iterations=1)
        
        # Find contours
        contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Filter contours
        valid_colonies = []
        for contour in contours:
            area = cv2.contourArea(contour)
            
            if self.min_area <= area <= self.max_area:
                perimeter = cv2.arcLength(contour, True)
                if perimeter > 0:
                    circularity = 4 * np.pi * area / (perimeter * perimeter)
                    
                    if circularity >= self.circularity_threshold:
                        x, y, w, h = cv2.boundingRect(contour)
                        aspect_ratio = float(w) / h if h > 0 else 0
                        
                        if 0.6 <= aspect_ratio <= 1.7:
                            valid_colonies.append(contour)
        
        # Create annotated image
        annotated = image.copy()
        cv2.drawContours(annotated, valid_colonies, -1, (0, 255, 0), 3)
        
        # Add numbers
        for i, contour in enumerate(valid_colonies, 1):
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.putText(annotated, str(i), (cx-15, cy+10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 3)
        
        # Add count text
        count_text = f"Colony Count: {len(valid_colonies)}"
        cv2.putText(annotated, count_text, (20, 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
        
        return valid_colonies, annotated, combined_mask
    
    def analyze_image(self, image_array):
        """Analyze image and return results"""
        colonies, annotated, mask = self.detect_colonies_with_color(image_array)
        
        areas = [cv2.contourArea(c) for c in colonies]
        results = {
            'total_count': len(colonies),
            'min_area': float(min(areas)) if areas else 0,
            'max_area': float(max(areas)) if areas else 0,
            'mean_area': float(np.mean(areas)) if areas else 0,
            'median_area': float(np.median(areas)) if areas else 0
        }
        
        return results, annotated


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/count', methods=['POST'])
def count_colonies():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'}), 400
        
        file = request.files['image']
        if file.filename == '':
            return jsonify({'error': 'No image selected'}), 400
        
        # Get parameters from form
        min_area = int(request.form.get('min_area', 220))
        max_area = int(request.form.get('max_area', 850))
        circularity = float(request.form.get('circularity', 0.65))
        
        # Read image
        image_bytes = file.read()
        nparr = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if image is None:
            return jsonify({'error': 'Invalid image file'}), 400
        
        # Process image
        counter = ColiformCounter(min_area, max_area, circularity)
        results, annotated = counter.analyze_image(image)
        
        # Convert annotated image to base64
        _, buffer = cv2.imencode('.jpg', annotated)
        img_base64 = base64.b64encode(buffer).decode('utf-8')
        
        return jsonify({
            'success': True,
            'count': results['total_count'],
            'stats': results,
            'annotated_image': img_base64
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
