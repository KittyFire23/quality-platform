from fastapi import FastAPI
from app.modules.users.routes import router as users_router

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