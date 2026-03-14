from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []
next_id = 1


@app.get("/todos")
def list_todos():
    return jsonify(todos)


@app.get("/todos/<int:todo_id>")
def get_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify(todo)


@app.post("/todos")
def create_todo():
    global next_id
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    todo = {
        "id": next_id,
        "title": data["title"],
        "done": False,
    }
    next_id += 1
    todos.append(todo)
    return jsonify(todo), 201


@app.patch("/todos/<int:todo_id>")
def update_todo(todo_id):
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    data = request.get_json()
    if "title" in data:
        todo["title"] = data["title"]
    if "done" in data:
        todo["done"] = data["done"]
    return jsonify(todo)


@app.delete("/todos/<int:todo_id>")
def delete_todo(todo_id):
    global todos
    todo = next((t for t in todos if t["id"] == todo_id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    todos = [t for t in todos if t["id"] != todo_id]
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
