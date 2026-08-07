# Task API

A simple REST API built with **FastAPI** that demonstrates CRUD (Create, Read, Update, Delete) operations on tasks.

This project was developed as part of a backend API assignment.

---

# Features

- Create a task
- Get all tasks
- Get a task by ID
- Update a task
- Delete a task
- Interactive Swagger UI documentation

---

# Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- Git
- GitHub

---

# API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API information |
| GET | `/health` | Check API health |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{id}` | Get a task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update an existing task |
| DELETE | `/tasks/{id}` | Delete a task |

---

# Example cURL Request

Create a new task:

```bash
curl -i -X POST http://127.0.0.1:8000/tasks ^
-H "Content-Type: application/json" ^
-d "{\"title\":\"Buy milk\"}"
```

Example Response:

```http
HTTP/1.1 201 Created
content-type: application/json

{
  "id": 4,
  "title": "Buy milk",
  "done": false
}
```

---

# HTTP Status Codes

| Status Code | Meaning |
|------------|---------|
| **200 OK** | Request completed successfully |
| **201 Created** | Task created successfully |
| **204 No Content** | Task deleted successfully |
| **400 Bad Request** | Invalid request body |
| **404 Not Found** | Task not found |

---

## Swagger UI

The interactive API documentation is available at:

http://127.0.0.1:8000/docs

### Screenshot

![Swagger UI](Images/swagger.png)

---

# Project Structure

```
API-task/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── images/
    └── swagger.png
```

---

# How to Test

You can test the API in two ways:

1. Using `curl -i` commands in the terminal.
2. Using the interactive Swagger UI available at `/docs`.

Both methods support the complete CRUD cycle:

- Create
- Read
- Update
- Delete
