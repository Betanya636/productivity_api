# Productivity Task Tracker API



## 1) Executive Summary



**Problem:**

People need a simple and lightweight way to track and manage tasks efficiently, including completing, updating, or deleting them, without requiring a full database backend or complex setup.



**Solution:**

The **Task Tracker** is a lightweight Flask API with an HTML/JavaScript frontend. Users can add, update, complete/un-complete, delete tasks, and view live statistics. All data is stored in memory for simplicity, making it fast and easy to run locally or via Docker.



---



## 2) System Overview



**Course Concept(s):**


* RESTful API development with Flask

* JSON data exchange between frontend and backend

* Optional containerization with Docker

### Architecture Diagram

!\[Architecture](assets/architecture.png)


**Data / Models / Services:**

**Data:** In-memory Python dictionary storing tasks

* **Sources:** User input through HTML frontend or API requests

**Size:** Minimal; stores only current tasks in memory

* **Format:** JSON

* **License:** MIT



---



## 3) How to Run (Local)



### Using Python (Local)



1. Activate virtual environment:



```powershell

.\\venv\\Scripts\\Activate.ps1

```



2. Run the Flask app:



```powershell

py app.py

```



3. Open your browser:



* Frontend: \[http://127.0.0.1:5000/index.html](http://127.0.0.1:5000/index.html)

* API endpoints: \[http://127.0.0.1:5000/tasks](http://127.0.0.1:5000/tasks)

* Stats: \[http://127.0.0.1:5000/tasks/stats](http://127.0.0.1:5000/tasks/stats)



---



### Docker 



```bash

\# build Docker image

docker build -t productivity\_api:latest .



\# run container

docker run --rm -p 5000:5000 productivity\_api:latest



\# health check

curl http://localhost:5000/tasks

```



---



## 4) Design Decisions



**Why this concept?**

I chose a Flask RESTful API because it is simple, lightweight, and easy to extend. It demonstrates core course concepts such as GET, POST, PUT, and DELETE endpoints without the overhead of a full database backend.



**Alternatives considered:**



* Full database backend (SQLite / MongoDB) — unnecessary for this simple project

* Django — too heavy; Flask is better for rapid development



**Tradeoffs:**



* **Performance:** Fast in-memory storage (but resets on restart)

* **Cost:** Zero — local tools only

* **Complexity:** Very simple

* * **Maintainability:** Easy to extend later



**Security / Privacy:**



* Basic input validation

* No sensitive data stored



**Ops:**



* Console-based logs

* Not built for production scale

* Known limitation: No persistent storage



---



## 5) Results \& Evaluation



### Task Tracker Screenshot



!\[Task Tracker Screenshot](assets/tracker.png)



### Sample Output



```json

{"id": 3, "title": "Do homework", "completed": false}

```



---



## 6) What’s Next

* Add persistent storage (SQLite or MongoDB)
* Add authentication
* Add task filtering, sorting, and search
* Deploy backend + frontend to cloud
* Improve logging and metrics
* Enhance UI and responsiveness

---



## 7) Links

**GitHub Repo:**

\[https://github.com/Betanya636/productivity\_api](https://github.com/Betanya636/productivity\_api) 

