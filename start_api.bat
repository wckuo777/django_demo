@echo off
echo 啟動 FastAPI Server 中...
start "" http://127.0.0.1:8001/docs
call .venv\Scripts\uvicorn.exe fastapi_app.main:app --reload --port 8001
pause