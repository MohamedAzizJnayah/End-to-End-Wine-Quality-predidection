# 🍷 Wine Quality Prediction Project  

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Framework-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikit-learn)](https://scikit-learn.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerization-blue?logo=docker)](https://www.docker.com/)
[![AWS](https://img.shields.io/badge/AWS-Deployment-orange?logo=amazonaws)](https://aws.amazon.com/)
[![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black?logo=githubactions)](https://github.com/features/actions)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📑 Table of Contents
1. [📘 Overview](#-overview)
2. [🌍 Live Demo](#-live-demo)
3. [🏗️ Project Structure](#️-project-structure)
4. [⚙️ Installation & Setup](#️-installation--setup)
5. [🐳 Docker Deployment](#-docker-deployment)
6. [🚀 CI/CD & Deployment](#-cicd--deployment)
7. [🧠 Machine Learning Workflow](#-machine-learning-workflow)
8. [📊 Model Performance](#-model-performance)
9. [🧩 Tech Stack](#-tech-stack)
10. [👨‍💻 Author](#-author)
11. [🏁 License](#-license)

---

## 📘 Overview  

**Wine Quality Prediction** is an **end-to-end Machine Learning project** that predicts wine quality based on physicochemical data.  
It follows **modern MLOps and software engineering best practices**, featuring:

- ✅ Modular architecture for scalability  
- 🌐 Flask API for serving predictions  
- ⚙️ CI/CD pipeline via **GitHub Actions**  
- ☁️ Deployment on **AWS** using **Docker**  

This project demonstrates a full ML lifecycle:
> Data ingestion → Preprocessing → Model training → Evaluation → Deployment  

---

## 🌍 Live Demo  

🧪 **Docker Hub Image:** [mohamedazizjnayah/wine_quality_prediction](https://hub.docker.com/r/mohamedazizjnayah/wine_quality_prediction)  
📂 **GitHub Repo:** [End-to-End-Wine-Quality-Predidection](https://github.com/MohamedAzizJnayah/End-to-End-Wine-Quality-predidection)

---

## 🏗️ Project Structure  
End-to-End-Wine-Quality-Prediction/
│
├── src/
│ ├── components/ # ML components: ingestion, transformation, training, evaluation
│ ├── config/ # Configuration management
│ ├── constant/ # Global constants
│ ├── entity/ # Custom entity classes
│ ├── logging/ # Logging setup
│ ├── pipeline/ # End-to-end ML pipelines
│ └── utils/ # Utility functions
│
├── config/ # Global configs
├── static/ # Static resources (CSS, JS, images)
├── templates/ # HTML templates for Flask web app
│
├── app.py # Flask web application
├── main.py # Main pipeline execution
├── setup.py # Setup script
├── template.py # Project structure generator
│
├── params.yaml # Model parameters and config
├── schema.yaml # Data schema validation
│
├── Dockerfile # Docker image configuration
├── requirements.txt # Python dependencies
└── README.md

## ⚙️ Installation & Setup
🧩 1. Clone the repository
git clone https://github.com/MohamedAzizJnayah/End-to-End-Wine-Quality-predidection.git
cd End-to-End-Wine-Quality-predidection

🧩 2. Create and activate a virtual environment
python -m venv venv
source venv/Scripts/activate   # Windows
# or
source venv/bin/activate       # macOS/Linux

🧩 3. Install dependencies
pip install -r requirements.txt

🧩 4. Run the Flask app
python app.py


The app runs by default on http://localhost:8080
.
You can change the port in app.py if needed.

## 🐳 Docker Deployment
🔹 Pull the pre-built Docker image
docker pull mohamedazizjnayah/wine_quality_prediction:latest

🔹 Run the container
docker run -p 8080:8080 mohamedazizjnayah/wine_quality_prediction:latest


✅ The app will be available at http://localhost:8080

## 🚀 CI/CD & Deployment

GitHub Actions for automated testing, linting, and deployment

Docker for consistent containerized environments

AWS (ECS / EC2) for scalable hosting

Pipeline Stages:

Build →

Test →

Dockerize →

Deploy

This ensures a fully automated and reliable continuous delivery process.

## 🧠 Machine Learning Workflow
Stage	Description
1. Data Ingestion	    : Load and validate raw wine dataset (CSV format)
2. Data Transformation	: Handle missing values, encode categorical features, scale numeric features
3. Model Training	    : Train models (RandomForest, XGBoost, etc.) and save the best
4. Evaluation	        : Compare models using RMSE, MAE, and R²
5. Deployment	        : Serve predictions through Flask REST API

## 🧩 Tech Stack
| Category | Technologies |
|-----------|--------------|
| **Programming Language** | Python |
| **Frameworks & Libraries** | Flask, Scikit-learn, Pandas, NumPy |
| **Deployment Tools** | Docker, AWS |
| **CI/CD** | GitHub Actions |
| **Configuration** | YAML |
| **Version Control** | Git & GitHub |


## 👨‍💻 Author  

**👤 Mohamed Aziz Jnayah**  
📍 *Machine Learning Engineer | MLOps Enthusiast*  

[![GitHub](https://img.shields.io/badge/GitHub-@MohamedAzizJnayah-black?logo=github)](https://github.com/MohamedAzizJnayah)
[![Docker Hub](https://img.shields.io/badge/Docker-mohamedazizjnayah-blue?logo=docker)](https://hub.docker.com/u/mohamedazizjnayah)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/mohamedazizjnayah/)
[![Email](https://img.shields.io/badge/Email-mohamedazizjnayah%40gmail.com-red?logo=gmail)](mailto:mohamedazizjnayah@gmail.com)


## 🏁 License

This project is licensed under the MIT License — feel free to use, modify, and distribute it for educational or commercial purposes.