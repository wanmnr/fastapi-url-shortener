# main.py

from fastapi import FastAPI
from app.settings.config import settings
from app.routes import user

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "debug": settings.debug,
        "database_url": settings.database_url
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)