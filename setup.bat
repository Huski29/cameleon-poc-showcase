@echo off
echo ========================================
echo   Cameleon Full Stack Setup
echo ========================================
echo.

echo [1/4] Setting up backend...
cd backend

echo [2/4] Creating virtual environment...
python -m venv venv

echo [3/4] Activating virtual environment and installing dependencies...
call venv\Scripts\activate
pip install -r requirements.txt

echo [4/4] Seeding database...
python seed.py

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo To start the application:
echo.
echo   1. Backend (Terminal 1):
echo      cd backend
echo      venv\Scripts\activate
echo      uvicorn app.main:app --reload --port 8000
echo.
echo   2. Frontend (Terminal 2):
echo      cd frontend
echo      npm install
echo      npm run dev
echo.
echo   Then visit: http://localhost:3000
echo ========================================

