
from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "task": "Complete Kubernetes lab", "completed": False},
    {"id": 2, "task": "Submit assignment", "completed": False}
]

@app.route("/")
def home():
    return jsonify({
        "message": "To-Do Application",
        "tasks": tasks
    })

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    if not data or not data.get("task"):
        return jsonify({"error": "Task name is required"}), 400

    new_task = {
        "id": max([t["id"] for t in tasks], default=0) + 1,
        "task": data["task"],
        "completed": False
    }

    tasks.append(new_task)
    return jsonify(new_task), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return jsonify(task)

    return jsonify({"error": "Task not found"}), 404

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
