## Pneumonia Detection API - LLM Project

This project implements a **Machine Learning model** for pneumonia detection from X-ray images. It includes a **Streamlit frontend** and a **FastAPI backend**, fully containerized using **Docker**. CI/CD is set up with **GitHub Actions**, and the images are deployed to **GitHub Container Registry (GHCR)**.

---

## Project Structure

- **Frontend**: Developed with **Streamlit**, provides a UI for users to upload X-ray images and get predictions.
- **Backend**: Built with **FastAPI**, loads a pre-trained CNN model to perform predictions and serves API endpoints.
- **Containerization (Docker)**: Both frontend and backend are containerized for easy deployment.
- **CI/CD**: Uses **GitHub Actions** for automatic builds and deployment.
- **Container Registry**: Both frontend and backend images are pushed to **GitHub Container Registry (GHCR)**.
- **Docker Compose**: Manages the services and ensures they run together.

---

## Features

✔ **Upload X-ray images** and get **pneumonia predictions**.  
✔ **Frontend & Backend separation**, connected via **API**.  
✔ **Automated Deployment** with **CI/CD & Docker**.  
✔ **Monitoring & Logging** using **Prometheus**.

---

## How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/llm-pneumonia-api.git
cd llm-pneumonia-api
```

### 2. Run the Project using Docker Compose 
```bash
docker-compose up -d
```
This will start both the frontend and backend containers.

### 3. Access the frontend
```bash
http://localhost:8501
```

### 4.Test the API
```bash
curl -X POST "http://localhost:8000/api/predict" -F "file=@test_image.png"
```

