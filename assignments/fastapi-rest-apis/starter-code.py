from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI REST APIs")

class TodoItem(BaseModel):
    id: int
    title: str = Field(..., min_length=1, description="Title of the todo item")
    completed: bool = False
    description: Optional[str] = None

# In-memory storage for todo items
todos: List[TodoItem] = [
    TodoItem(id=1, title="Learn FastAPI", completed=False, description="Read the docs and build an API"),
]

@app.get("/", summary="Home message")
def read_root() -> dict:
    return {"message": "Welcome to the FastAPI REST API assignment"}

@app.get("/todos", response_model=List[TodoItem], summary="List todo items")
def list_todos() -> List[TodoItem]:
    return todos

@app.post("/todos", response_model=TodoItem, summary="Create a todo item")
def create_todo(item: TodoItem) -> TodoItem:
    if any(todo.id == item.id for todo in todos):
        raise HTTPException(status_code=400, detail="Todo item with this id already exists")
    todos.append(item)
    return item

@app.put("/todos/{todo_id}", response_model=TodoItem, summary="Update a todo item")
def update_todo(todo_id: int, item: TodoItem) -> TodoItem:
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = item
            return item
    raise HTTPException(status_code=404, detail="Todo item not found")

@app.delete("/todos/{todo_id}", summary="Delete a todo item")
def delete_todo(todo_id: int) -> dict:
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"detail": "Todo item deleted"}
    raise HTTPException(status_code=404, detail="Todo item not found")

# To run this app locally:
# uvicorn starter-code:app --reload
