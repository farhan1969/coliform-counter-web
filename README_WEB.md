# Fecal Coliform Colony Counter - Web Application

A beautiful web interface for counting fecal coliform colonies from images.

## 🚀 Features

- **User-Friendly Interface**: Simple drag-and-drop or click to upload
- **Real-Time Processing**: Get results instantly
- **Customizable Parameters**: Adjust detection settings
- **Visual Results**: See annotated images with numbered colonies
- **Statistics**: Get detailed colony size information

## 📋 Requirements

- Python 3.8 or higher
- Web browser (Chrome, Firefox, Safari, Edge)

## 🔧 Installation

### Option 1: Run Locally on Your Computer

1. **Download all files** and put them in a folder:
   ```
   colony-counter-web/
   ├── app.py
   ├── requirements.txt
   ├── templates/
   │   └── index.html
   ├── uploads/      (will be created automatically)
   └── results/      (will be created automatically)
   ```

2. **Install Python requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open your browser:**
   - Go to: `http://localhost:5000`
   - You should see the Colony Counter interface!

### Option 2: Deploy Online (Free Hosting)

#### Deploy to Render.com (FREE):

1. **Create account** at https://render.com

2. **Upload your files** to GitHub (or use Render's direct upload)

3. **Create new Web Service:**
   - Connect your repository
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`

4. **Add to requirements.txt:**
   ```
   gunicorn==21.2.0
   ```

5. Your app will be live at: `https://your-app-name.onrender.com`

#### Deploy to PythonAnywhere (FREE):

1. **Sign up** at https://www.pythonanywhere.com

2. **Upload files** via Files tab

3. **Install requirements** in Bash console:
   ```bash
   pip install --user -r requirements.txt
   ```

4. **Configure Web app:**
   - Go to Web tab
   - Add new web app (Flask)
   - Point to your app.py file

5. Your app will be at: `https://yourusername.pythonanywhere.com`

#### Deploy to Heroku (FREE tier available):

1. **Create** `Procfile` (no extension):
   ```
   web: gunicorn app:app
   ```

2. **Add gunicorn** to requirements.txt

3. **Deploy via Heroku CLI:**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

## 📱 How to Use

1. **Upload Image:**
   - Click "Choose Image" or drag & drop your coliform plate photo
   - Supports: JPG, PNG, HEIC formats

2. **Adjust Parameters (Optional):**
   - **Minimum Colony Size**: Lower = detects smaller colonies (default: 220)
   - **Maximum Colony Size**: Higher = includes bigger colonies (default: 850)
   - **Circularity**: Higher = only round colonies (default: 0.65)

3. **Count Colonies:**
   - Click "Count Colonies" button
   - Wait a few seconds for processing

4. **View Results:**
   - Total colony count
   - Size statistics
   - Annotated image with numbered colonies

## 🎯 Parameter Guide

### For Different Colony Sizes:

**Small colonies (detect all):**
```
Minimum: 10
Maximum: 850
Circularity: 0.45
```

**Medium colonies (balanced):**
```
Minimum: 50
Maximum: 850
Circularity: 0.55
```

**Large colonies only (default):**
```
Minimum: 220
Maximum: 850
Circularity: 0.65
```

## 🖼️ Image Tips

For best results:
- Use good lighting
- White background
- High resolution (at least 1000x1000 pixels)
- Minimal shadows
- Clean plate (no debris)

## 🔒 Security Notes

- Maximum upload size: 16MB
- Images are processed in memory
- Files are temporarily stored but can be deleted after processing

## 🛠️ Troubleshooting

**"Module not found" error:**
```bash
pip install --upgrade -r requirements.txt
```

**Port already in use:**
- Change port in app.py: `app.run(port=5001)`

**Large images timing out:**
- Resize images before uploading (recommended: max 2000x2000)

## 📊 Advanced: API Usage

You can also use the app programmatically:

```python
import requests

url = 'http://localhost:5000/count'
files = {'image': open('your_image.jpg', 'rb')}
data = {
    'min_area': 220,
    'max_area': 850,
    'circularity': 0.65
}

response = requests.post(url, files=files, data=data)
result = response.json()

print(f"Colony Count: {result['count']}")
```

## 🌐 Making it Accessible Online

### Quick Options:

1. **ngrok** (Temporary public URL):
   ```bash
   # Install ngrok
   pip install pyngrok
   
   # Run your app
   python app.py
   
   # In another terminal
   ngrok http 5000
   ```
   Share the ngrok URL with others!

2. **LocalTunnel** (Temporary):
   ```bash
   npm install -g localtunnel
   lt --port 5000
   ```

3. **Permanent hosting**: Use Render, PythonAnywhere, or Heroku (see above)

## 📞 Support

If you encounter issues:
1. Check Python version: `python --version` (should be 3.8+)
2. Verify all files are in correct structure
3. Check browser console for JavaScript errors
4. Try a different browser

## 🎨 Customization

You can customize the appearance by editing `templates/index.html`:
- Change colors in the `<style>` section
- Modify text and labels
- Add your logo or branding

## 📝 License

Free to use for personal and educational purposes.
