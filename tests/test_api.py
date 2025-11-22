import requests

BASE = "http://127.0.0.1:5000"

# Add a task
response = requests.post(f"{BASE}/tasks", json={"title": "Do homework"})
print("POST /tasks:", response.json())

# List tasks
response = requests.get(f"{BASE}/tasks")
print("GET /tasks:", response.json())

# Complete the task with ID 1
response = requests.put(f"{BASE}/tasks/1/complete")
print("PUT /tasks/1/complete:", response.json())

# Update the task title
response = requests.put(f"{BASE}/tasks/1", json={"title": "New homework title"})
print("PUT /tasks/1:", response.json())

# Get stats
response = requests.get(f"{BASE}/tasks/stats")
print("GET /tasks/stats:", response.json())

# Delete task
response = requests.delete(f"{BASE}/tasks/1")
print("DELETE /tasks/1:", response.json())
