from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.todos import router as todos_router

app = FastAPI(title="Todo Starter App")

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(todos_router)
