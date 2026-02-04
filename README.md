# 🔬 Fecal Coliform Colony Counter

Automatic colony counting from petri dish images using computer vision.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)

## 🌟 Features

- **Automatic Detection**: AI-powered colony recognition
- **Web Interface**: Beautiful, easy-to-use interface
- **Adjustable Parameters**: Fine-tune detection sensitivity
- **Visual Results**: Annotated images with numbered colonies
- **Statistics**: Detailed colony size analysis
- **Mobile Friendly**: Works on any device

## 🚀 Quick Start

### Option 1: Run Locally

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/coliform-counter.git
cd coliform-counter

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Open browser to http://localhost:5000
```

### Option 2: Deploy Online (FREE)

#### Deploy to Render.com (Recommended)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

1. Click the button above
2. Connect your GitHub account
3. Deploy automatically!

Your app will be live at: `https://your-app.onrender.com`

## 📸 How to Use

1. **Upload Image**: Drag & drop or click to upload your petri dish photo
2. **Adjust Parameters** (optional)
3. **Count Colonies**: Click the button and get instant results
4. **View Results**: See total count, statistics, and annotated image

## 🎯 Parameter Guide

| Use Case | Min Size | Max Size | Circularity |
|----------|----------|----------|-------------|
| All colonies | 10 | 850 | 0.45 |
| Medium-large | 50 | 850 | 0.55 |
| Large only | 220 | 850 | 0.65 |

## 🛠️ Technology Stack

- **Backend**: Flask (Python)
- **Image Processing**: OpenCV, NumPy
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Gunicorn

## 📋 Requirements

- Python 3.8+
- OpenCV, NumPy, Flask, Pillow

## 📞 Support

See [QUICK_START.md](QUICK_START.md) and [GITHUB_DEPLOY.md](GITHUB_DEPLOY.md) for detailed instructions.

---

Made with ❤️ for microbiologists and researchers
