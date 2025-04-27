from fastapi import FastAPI
from fastapi_app.api.v1 import fruits
from fastapi.responses import HTMLResponse
from fastapi_app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
# 加入 CORS middleware
origins = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    # 如果你還有其他 domain 或 port 要允許，就加在這裡
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,        # 或者 ["*"]（開發時用，生產環境不要用*）
    allow_credentials=True,
    allow_methods=["*"],          # 允許所有 HTTP 方法
    allow_headers=["*"],          # 允許所有自訂 Header
)
# 載入 API routers
app.include_router(fruits.router, prefix="/api/v1/fruits", tags=["fruits"])
# 啟動時自動建立資料表
Base.metadata.create_all(bind=engine)
@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = """
    <html>
        <head>
            <title>FastAPI 服務首頁</title>
            <style>
                body { font-family: Arial, sans-serif; padding: 2rem; background-color: #f0f0f0; }
                h1 { color: #333; }
                ul { list-style-type: none; padding: 0; }
                li { margin: 1rem 0; }
                a { text-decoration: none; font-size: 1.2rem; color: #007ACC; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <h1>FastAPI API 首頁</h1>
            <ul>
                <li><a href="/docs" target="_blank">Swagger API 文件</a></li>
                <li><a href="/api/v1/fruits" target="_blank">get 資料清單 API</a></li>
            </ul>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
    # return "<h1>Welcome to Ben's Demo FastAPI Server!</h1><p>Go to <a href='/docs'>API Docs</a></p>"