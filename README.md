\# Productivity Task Tracker API



\## 1) Executive Summary



\*\*Problem:\*\*  

People need a simple and lightweight way to track and manage tasks efficiently, including completing, updating, or deleting them, without requiring a full database backend or complex setup.



\*\*Solution:\*\*  

The \*\*Task Tracker\*\* is a lightweight Flask API with an HTML/JavaScript frontend. Users can add, update, complete/un-complete, delete tasks, and view live statistics. All data is stored in memory for simplicity, making it fast and easy to run locally or via Docker.



---



\## 2) System Overview



\*\*Course Concept(s):\*\*  

\- RESTful API development with Flask  

\- JSON data exchange between frontend and backend  

\- Optional containerization with Docker  



\*\*Architecture Diagram:\*\*  



\## Architecture Diagram

!\[Architecture](assets/architecture.png)



\*\*Data / Models / Services:\*\*  

\- \*\*Data:\*\* In-memory Python dictionary storing tasks  

\- \*\*Sources:\*\* User input through HTML frontend or API requests  

\- \*\*Size:\*\* Minimal; stores only current tasks in memory  

\- \*\*Format:\*\* JSON  

\- \*\*License:\*\* MIT  



---



\## 3) How to Run (Local)



\### Using Python (Local)

1\. Activate virtual environment:

```powershell

.\\venv\\Scripts\\Activate.ps



2\. Run the Flask app: 

py app.py



3\. Open your browers:

Frontend: http://127.0.0.1:5000/index.html

API endpoints: http://127.0.0.1:5000/tasks

Stats: http://127.0.0.1:5000/tasks/stats



\### Docker (optional)

```bash

\# build Docker image

docker build -t productivity\_api:latest .

\# run container

docker run --rm -p 5000:5000 productivity\_api:latest

\# health check

curl http://localhost:5000/tasks



\## 4) Design Decisions



\*\*Why this concept?\*\*  

I chose a Flask RESTful API because it is simple, lightweight, and easy to extend. It allows me to demonstrate core course concepts such as GET, POST, PUT, and DELETE endpoints without the overhead of a full database backend.



\*\*Alternatives considered:\*\*  

\- Full database backend (SQLite/MongoDB) was considered but deemed overkill for a small, local project.  

\- Other frameworks like Django were considered but Flask offered a simpler, more lightweight approach.



\*\*Tradeoffs:\*\*  

\- \*\*Performance:\*\* Fast in-memory storage, but not persistent across restarts  

\- \*\*Cost:\*\* Minimal (no external services required)  

\- \*\*Complexity:\*\* Simple and maintainable  

\- \*\*Maintainability:\*\* Easy to modify and extend in future iterations



\*\*Security / Privacy:\*\*  

\- Input validation for task titles to prevent invalid entries  

\- No PII or sensitive data is stored  



\*\*Ops:\*\*  

\- Logs: Basic console output  

\- Scaling: Currently limited to local use; not suitable for production-scale  

\- Known limitations: Tasks are lost when the server restarts, and no authentication is implemented



---



\## 5) Results \& Evaluation



Here is a screenshot of the Task Tracker sample:



\### Task Tracker

!\[Task Tracker Screenshot](assets/tracker.png)



Test Example:  



Added task JSON:

```json

{"id":3,"title":"Do homework","completed":false}



\## 6) What’s Next



\*\*Planned Improvements / Refactors / Stretch Features:\*\*  

\- Add persistent storage using SQLite or MongoDB  

\- Implement user authentication and accounts  

\- Add task filtering, sorting, and search features  

\- Deploy backend and frontend to the cloud (Docker or other hosting)  

\- Improve logging, metrics, and error handling  

\- Enhance frontend for better user experience and responsiveness



\## 7) Links

\*\*GitHub Repo:\*\* \[https://github.com/Betanya636/productivity\_api](https://github.com/Betanya636/productivity\_api)  

