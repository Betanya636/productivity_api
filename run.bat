@echo off
REM Stop any existing container
docker rm -f productivity-api >nul 2>&1

REM Build Docker image
docker build -t productivity-api .

REM Start Docker container in a new window
start "Backend" cmd /k "docker run --name productivity-api -p 5000:5000 productivity-api"

REM Wait a few seconds for backend to start
timeout /t 5

REM Start frontend server in a new window
start "Frontend" cmd /k "python -m http.server 8000"

echo Done! Open your browser at http://127.0.0.1:8000/index.html
pause
