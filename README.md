# Python To-Do API

A simple REST API for managing to-do items, built with Flask.

## Endpoints

| Method   | Path             | Description         |
|----------|------------------|---------------------|
| `GET`    | `/todos`         | List all to-dos     |
| `GET`    | `/todos/<id>`    | Get a single to-do  |
| `POST`   | `/todos`         | Create a to-do      |
| `PATCH`  | `/todos/<id>`    | Update a to-do      |
| `DELETE` | `/todos/<id>`    | Delete a to-do      |

### Request/Response Examples

**Create a to-do:**

```bash
curl -X POST http://localhost:5000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries"}'
```

```json
{"id": 1, "title": "Buy groceries", "done": false}
```

**Mark it done:**

```bash
curl -X PATCH http://localhost:5000/todos/1 \
  -H "Content-Type: application/json" \
  -d '{"done": true}'
```

**List all to-dos:**

```bash
curl http://localhost:5000/todos
```

## Getting Started

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Server

```bash
python app.py
```

The server starts at `http://localhost:5000` with debug mode enabled.

## Running Tests

```bash
pip install pytest
pytest -v
```
