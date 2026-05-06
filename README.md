# 🚀 Dockerised "Quote of the Day" API

A lightweight Python microservice that serves random tech quotes, fully containerized with Docker and automated using GitHub Actions CI/CD.

---

## 📌 Overview

This project demonstrates how to:

* Build a simple REST API using Flask
* Containerise an application with Docker
* Automate builds and deployments using GitHub Actions
* Push Docker images to Docker Hub

---

## 🧠 The Hook

**Demonstrates containerisation and automated build pipelines—the foundation of modern cloud deployment.**

---

## ⚙️ Tech Stack

* Python (Flask)
* Docker
* GitHub Actions (CI/CD)
* Docker Hub (Image Registry)

---

## 📁 Project Structure

```
.
├── app.py
├── Dockerfile
└── .github/
    └── workflows/
        └── docker-build.yml
```

---

## 🧩 API Endpoint

### GET `/quote`

Returns a random tech quote.

### Example Response:

```json
{
  "quote": "Talk is cheap. Show me the code. - Linus Torvalds"
}
```

---

## 🐳 Running Locally with Docker

### 1. Build the image

```bash
docker build -t my-quote-app .
```

### 2. Run the container

```bash
docker run -p 5000:5000 my-quote-app
```

### 3. Test the API

Open in browser:

```
http://localhost:5000/quote
```

---

## 🔄 CI/CD Pipeline (GitHub Actions)

This project uses GitHub Actions to:

* Build the Docker image on every push to `main`
* Authenticate with Docker Hub
* Push the latest image automatically

Workflow file:

```
.github/workflows/docker-build.yml
```

---

## 📦 Docker Hub Image

👉 https://hub.docker.com/r/kattran177/my-quote-app

Pull and run directly:

```bash
docker pull kattran177/my-quote-app:latest
docker run -p 5000:5000 kattran177/my-quote-app
```

---

## ✅ Proof of Work

* Automated CI/CD pipeline via GitHub Actions
* Live Docker image hosted on Docker Hub
* Fully reproducible containerized environment

---

## 🚧 Future Improvements

* Add more API endpoints (e.g., categories of quotes)
* Use a database instead of hardcoded quotes
* Deploy to a cloud platform (Render, Fly.io, AWS)
* Add unit tests and linting to CI pipeline

---

## 📚 What I Learned

- How Docker images are built and layered
- How CI/CD pipelines automate deployment workflows
- How to securely use secrets in GitHub Actions