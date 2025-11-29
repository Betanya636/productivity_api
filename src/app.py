from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import os

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "templates"))
CORS(app)

# In-memory list of tasks with seed/test data
tasks = []
next_id = 1

@app.route('/')
def home():
    return render_template('index.html')

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False
    }
    tasks.append(task)
    return jsonify(task), 201

# Mark a task as complete
@app.route("/tasks/<int:task_id>/complete", methods=["PUT"])
def toggle_complete_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if not task:
        return {"error": "Task not found"}, 404
    # Toggle completed status
    task["completed"] = not task["completed"]
    return task

# Mark a task as incomplete
@app.route('/tasks/<int:task_id>/incomplete', methods=['PUT'])
def mark_incomplete(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = False
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

# Update a task's title
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.get("title", task["title"])
            return jsonify(task)
    return jsonify({"error": "Task not found"}), 404

# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted"})
    return jsonify({"error": "Task not found"}), 404

# Get task stats
@app.route('/tasks/stats', methods=['GET'])
def task_stats():
    total = len(tasks)
    completed = len([t for t in tasks if t["completed"]])
    incomplete = total - completed
    return jsonify({
        "total_tasks": total,
        "completed_tasks": completed,
        "incomplete_tasks": incomplete
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
