@echo off
echo ========================================
echo Fecal Coliform Colony Counter Web App
echo ========================================
echo.
echo Installing requirements...
pip install -r requirements.txt
echo.
echo Starting web server...
echo.
echo The app will open at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py
pause
