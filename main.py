from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse


app = FastAPI()

tasks = [

    {"id": 1, "title": "Task 1", "done": False},
    {"id": 2, "title": "Task 2", "done": True},
    {"id": 3, "title": "Task 3", "done": False}

]

@app.get("/")
def root():
    return {"name": "Task API",
            "version": "1.0",
            "endpoints": [
                "/tasks"
            ]}
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{id}")
def get_task(id: int):
    for task in tasks:
        if task["id"] == id:
            return task
    return {"error": "Task not found"}, 404

class TaskCreate(BaseModel):
    title: str | None=None

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    if not task.title or not task.title.strip():
       return JSONResponse (
           status_code=400,
              content={"error": "Title is required"}
       )
    new_task = {"id": len(tasks) + 1, "title": task.title, "done": False}
    tasks.append(new_task)
    return new_task