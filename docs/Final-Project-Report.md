# CloudOps Enterprise Platform
## Cloud Infrastructure, Automation and Deployment Project

### 1. Project Overview
This project demonstrates a basic CloudOps and DevOps workflow using a Python web application, Docker containerization, automated testing, and GitHub Actions.

### 2. Objectives
- Develop and run a simple web application.
- Package the application using Docker.
- Configure a Docker health check.
- Automate build and test tasks using GitHub Actions.
- Verify application availability locally.

### 3. Technologies Used
- Python 3.11
- Docker
- Git and GitHub
- GitHub Actions
- PowerShell
- Visual Studio Code

### 4. Application Description
The Python application runs an HTTP server on port 8000 and displays a welcome page for the Cloud Computing and DevOps internship project.

### 5. Docker Implementation
The application is packaged into a Docker image named `cloudops-app:latest`. The container exposes port 8000 and runs the Python application.

A Docker health check is configured to test whether the application responds to an HTTP request.

### 6. Continuous Integration
A GitHub Actions workflow automates project checks when code changes are pushed to the repository. A successful workflow run was verified on GitHub.

### 7. Testing and Verification
- The local web application returned HTTP 200 OK.
- The Docker container health status returned `healthy`.
- The GitHub Actions workflow completed successfully.
- A test file named `test_app.py` is included in the project.

### 8. Evidence and Screenshots
The following screenshots are included in the project folder:

- `website-screenshot.png` — application running in the browser.
- `docker-health.png` — Docker container health status.
- `github-actions.png` — successful GitHub Actions run.

### 9. Limitations
The application was tested locally using Docker. A production cloud deployment, Kubernetes deployment, monitoring dashboard, serverless services, and Big Data or machine-learning integration have not been verified as completed components.

### 10. Conclusion
This project demonstrates foundational CloudOps practices, including application containerization, health monitoring, source control, and automated workflow execution. It provides a starting point for future deployment to cloud infrastructure and expansion into orchestration and monitoring.

### 11. How to Run
Build the Docker image:

```powershell
docker build -t cloudops-app:latest .
```

Start the existing container:

```powershell
docker start cloudops-healthcheck
```

Open the application:

http://localhost:8000

Check container health:

```powershell
docker inspect --format="{{.State.Health.Status}}" cloudops-healthcheck
```