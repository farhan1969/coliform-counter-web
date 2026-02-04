# 🚀 QUICK START GUIDE

## Run Locally (Easiest Method)

### Windows:
1. Double-click `start_windows.bat`
2. Wait for it to install requirements
3. Browser will open automatically or go to: http://localhost:5000

### Mac/Linux:
1. Open Terminal
2. Navigate to the folder: `cd /path/to/folder`
3. Run: `./start_mac_linux.sh`
4. Go to: http://localhost:5000

### Manual Start:
```bash
# Install requirements (first time only)
pip install -r requirements.txt

# Run the app
python app.py

# Open browser to: http://localhost:5000
```

---

## Deploy Online (Free Forever!)

### Method 1: PythonAnywhere (Recommended - FREE & Easy)

1. **Sign up**: https://www.pythonanywhere.com (free account)

2. **Upload files**:
   - Go to "Files" tab
   - Upload: `app.py`, `requirements.txt`, and `templates` folder

3. **Install requirements**:
   - Open "Bash" console
   - Run: `pip install --user flask opencv-python numpy pillow`

4. **Setup web app**:
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose Flask
   - Python version: 3.10
   - Path to app: `/home/yourusername/app.py`
   - Click "Reload"

5. **Your app is live!**
   - URL: `https://yourusername.pythonanywhere.com`
   - Share this link with anyone!

### Method 2: Render.com (FREE)

1. **Sign up**: https://render.com

2. **Create Web Service**:
   - Click "New +" → "Web Service"
   - Connect GitHub or upload files
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`

3. **Add to requirements.txt**:
   ```
   gunicorn==21.2.0
   ```

4. **Deploy!**
   - Your app: `https://your-app-name.onrender.com`

### Method 3: Quick Share (Temporary URL)

Using **ngrok** (no signup needed):

```bash
# Install ngrok
pip install pyngrok

# Run your app
python app.py

# In another terminal
ngrok http 5000
```

You'll get a public URL like: `https://abc123.ngrok.io`
Share this URL and anyone can use your app!

---

## How to Use the Web App

1. **Open the website** (localhost:5000 or your online URL)

2. **Upload image**:
   - Click "Choose Image" or drag & drop
   - Supports: JPG, PNG, HEIC

3. **Adjust settings** (optional):
   - Minimum Size: 220 (default)
   - Maximum Size: 850 (default)
   - Circularity: 0.65 (default)

4. **Click "Count Colonies"**

5. **See results**:
   - Total count
   - Statistics
   - Annotated image

---

## Troubleshooting

**Can't install packages?**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Port 5000 already in use?**
- Edit `app.py` line: `app.run(port=5001)`

**App not working online?**
- Check all files uploaded correctly
- Verify Python version is 3.8+
- Check hosting platform logs

---

## Need Help?

Check the full README_WEB.md for detailed instructions!
