from fastapi import FastAPI
from app.modules.users.routes import router as users_router
from app.modules.processes.routes import router as processes_router
from app.modules.sectors.routes import router as sectors_router
from app.core.config import DATABASE_URL
from database.connection import engine
from app.modules.employees.routes import router as employees_router
from app.modules.machines.routes import router as machines_router
from app.modules.templates.routes import router as templates_router
from app.modules.questions.routes import router as questions_router

app = FastAPI(
    title="Quality Platform",
    version="1.0.0"
)

app.include_router(
    users_router,
    prefix="/users",
    tags=["Users"]
)

app.include_router(
    processes_router,
    prefix="/processes",
    tags=["Processes"]
)
app.include_router(
    sectors_router,
    prefix="/sectors",
    tags=["Sectors"]
)
app.include_router(
    employees_router,
    prefix="/employees",
    tags=["Employees"]
)
app.include_router(
    machines_router,
    prefix="/machines",
    tags=["Machines"]
)
app.include_router(
    templates_router,
    prefix="/templates",
    tags=["Templates"]
)
app.include_router(
    questions_router,
    prefix="/questions",
    tags=["Questions"]
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