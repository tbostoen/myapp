from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.services.todo_store import add_todo, delete_todo, get_all_todos

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def home(request: Request):
    todos = get_all_todos()
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"todos": todos},
    )


@router.post("/todos")
def create_todo(text: str = Form(...)):
    add_todo(text)
    return RedirectResponse(url="/", status_code=303)


@router.post("/todos/{todo_id}/delete")
def remove_todo(todo_id: int):
    delete_todo(todo_id)
    return RedirectResponse(url="/", status_code=303)
