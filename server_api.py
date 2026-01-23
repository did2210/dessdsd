from fastapi import FastAPI
import uvicorn
from datetime import datetime

app = FastAPI(title="Test API", description="API для проверки прокси")

@app.get("/")
async def root():
    return {"message": "FastAPI работает!", "timestamp": str(datetime.now())}

@app.get("/test")
async def test():
    return {
        "status": "ok",
        "port": 8000,
        "message": "Это тестовое API для проверки прокси",
        "server_time": str(datetime.now())
    }

@app.get("/api/tags")
async def api_tags():
    # Совместимость с Ollama API для теста
    return {
        "models": [
            {
                "name": "test-model:latest",
                "size": 0,
                "modified_at": str(datetime.now())
            }
        ]
    }

if __name__ == "__main__":
    # Запускаем на всех интерфейсах
    uvicorn.run(app, host="0.0.0.0", port=8000)
