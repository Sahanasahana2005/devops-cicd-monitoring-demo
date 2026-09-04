# devops-cicd-monitoring-demo
# DevOps, CI/CD & Monitoring Pipeline Project

This repository demonstrates an end-to-end DevOps automated pipeline with Continuous Integration (CI), Continuous Deployment (CD), and health monitoring.

## 🚀 Workflow Pipeline Architecture

`GitHub Push` ➔ `Automated Testing (Pytest)` ➔ `Build Docker Image` ➔ `Deploy & Health Check`

## 🛠️ Components
- **Application**: Python Flask REST API
- **Testing**: Automated Pytest suite
- **Containerization**: Dockerfile setup
- **CI/CD Automation**: GitHub Actions workflow (`ci-cd.yml`)
- **Observability**: Healthcheck monitoring endpoint (`/health`)
