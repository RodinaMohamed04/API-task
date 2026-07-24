from fastapi import FastAPI

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