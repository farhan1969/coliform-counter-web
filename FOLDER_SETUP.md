# 📁 FOLDER STRUCTURE SETUP

## Important: How to Organize Your Files

When you download all the files, you need to organize them in this **exact structure**:

```
colony-counter-web/              ← Create this main folder
│
├── app.py                       ← Download this file
├── requirements.txt             ← Download this file
├── start_windows.bat            ← Download this file (Windows users)
├── start_mac_linux.sh           ← Download this file (Mac/Linux users)
├── QUICK_START.md              ← Download this file
├── README_WEB.md               ← Download this file
├── WEB_APP_SUMMARY.md          ← Download this file
│
└── templates/                   ← CREATE THIS FOLDER
    └── index.html               ← Put the index.html file HERE
```

## 🔴 CRITICAL: Templates Folder

**You MUST create a folder called `templates`** and put `index.html` inside it!

### Step-by-Step Setup:

1. **Create main folder:**
   - Name it: `colony-counter-web` (or any name you want)

2. **Download these files** and put them in the main folder:
   - app.py
   - requirements.txt
   - start_windows.bat (or start_mac_linux.sh)
   - All the .md files

3. **Create `templates` folder:**
   - Inside `colony-counter-web`, create a new folder
   - Name it exactly: `templates` (lowercase, plural)

4. **Put index.html in templates folder:**
   - Download `index.html`
   - Move it into the `templates` folder

### Final Structure Should Look Like:

```
colony-counter-web/
│
├── app.py                    ✅
├── requirements.txt          ✅
├── start_windows.bat         ✅
├── templates/                ✅ Folder
│   └── index.html            ✅ Inside templates folder
```

## ✅ Quick Check:

Open your `colony-counter-web` folder. You should see:
- Several .py and .txt files
- A folder named `templates`
- Inside `templates`: one file called `index.html`

## ⚠️ Common Mistakes:

❌ **Wrong:** index.html in main folder
```
colony-counter-web/
├── index.html        ← WRONG LOCATION!
```

✅ **Correct:** index.html inside templates folder
```
colony-counter-web/
└── templates/
    └── index.html    ← CORRECT!
```

❌ **Wrong:** Folder named "template" (singular)
❌ **Wrong:** Folder named "Templates" (capital T)
✅ **Correct:** Folder named "templates" (lowercase, plural)

## 🚀 After Setup:

Once your folders are organized correctly:

**Windows:**
- Double-click `start_windows.bat`

**Mac/Linux:**
- Open Terminal
- Navigate to folder: `cd /path/to/colony-counter-web`
- Run: `./start_mac_linux.sh`

**Or manually:**
```bash
python app.py
```

Then open browser to: **http://localhost:5000**

## 🌐 For Online Deployment:

When uploading to PythonAnywhere or other hosting:
- Upload ALL files maintaining the same structure
- Make sure `templates` folder is uploaded with `index.html` inside it

## ❓ Need Help?

If you see error like "TemplateNotFound: index.html":
- ✅ Check: Is there a `templates` folder?
- ✅ Check: Is `index.html` inside the `templates` folder?
- ✅ Check: Are you running `app.py` from the main folder (not inside templates)?

That's it! The folder structure is critical for Flask to find the HTML file.
