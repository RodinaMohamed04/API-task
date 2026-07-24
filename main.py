from fastapi import FastAPI, Response
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
class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None

@app.put("/tasks/{id}")
def update_task(id: int, task: TaskUpdate):
    if (task.title is None and task.done is None):
        return JSONResponse(
            status_code=400,
            content={"error": "The body cannot be empty"}
        )
    if (task.title is not None and not task.title.strip()):
        return JSONResponse(
            status_code=400,
            content={"error": "Title cannot be empty"}
        )
    for t in tasks:
        if t["id"] == id:
            if task.title is not None:
                t["title"] = task.title
            if task.done is not None:
                t["done"] = task.done
            return t
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {id} not found"}
        )

@app.delete("/tasks/{id}", status_code=204)
def delete_task(id: int):
    for t in tasks:
        if t["id"] == id:
            tasks.remove(t)
            return Response(status_code=204)
        return JSONResponse(
            status_code=404,
            content={"error": f"Task {id} not found"}
        )