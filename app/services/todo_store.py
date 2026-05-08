from dataclasses import dataclass
from typing import List


@dataclass
class Todo:
    id: int
    text: str


_todos: List[Todo] = []
_next_id = 1


def get_all_todos() -> List[Todo]:
    return list(_todos)


def add_todo(text: str) -> None:
    global _next_id
    cleaned_text = text.strip()
    if not cleaned_text:
        return

    _todos.append(Todo(id=_next_id, text=cleaned_text))
    _next_id += 1


def delete_todo(todo_id: int) -> None:
    global _todos
    _todos = [todo for todo in _todos if todo.id != todo_id]
