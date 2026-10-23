from fastapi import FastAPI
from app.modules.users.routes import router as users_router
from app.core.config import DATABASE_URL
from database.connection import engine

app = FastAPI(
    title="Quality Platform",
    version="1.0.0"
)

app.include_router(
    users_router,
    prefix="/users",
    tags=["Users"]
)

@app.get("/")
def root():
    return {"message": "Quality Platform API"}

@app.get("/database")
def database():
    return {"database_url": DATABASE_URL}

@app.get("/connection")
def connection():
    return {"status": "Connection object created"}