# Jenkins-Project-2: Flask CRUD Application Deployment with CI/CD Pipeline

## Project Overview:

Welcome to our Flask CRUD Application Deployment project! In this project, we'll develop a Flask application with CRUD (Create, Read, Update, Delete) functionality for managing items. The application will be deployed using a CI/CD pipeline orchestrated by Jenkins. Our goal is to automate the build, test, and deployment processes while ensuring the reliability and scalability of our application.

## Objectives:

- **Flask CRUD Application Development:** Develop a Flask application with CRUD functionality for managing items in a database.
  
- **CI/CD Pipeline Setup:** Implement a Continuous Integration/Continuous Deployment (CI/CD) pipeline using Jenkins to automate the build, test, and deployment processes of the Flask application.
  
- **Deployment to AWS:** Deploy the Flask application to AWS ECS (Elastic Container Service) using Docker containers.

## Tools and Technologies:

- **Flask:** Python web framework for building the CRUD application.
- **DynamoDB:** NoSQL database service from AWS for storing application data.
- **Jenkins:** CI/CD automation server for orchestrating the pipeline.
- **Docker:** Containerization technology for packaging the application.
- **AWS ECS:** Container orchestration service for deploying and managing Docker containers.

## Project Structure:

- **app.py:** Main Python file containing the Flask application logic.
- **create_ecr.py:** Python script to create an ECR (Elastic Container Registry) repository.
- **create_ecs_cluster.py:** Python script to create an ECS (Elastic Container Service) cluster.
- **Dockerfile:** Configuration file for building the Docker image of the Flask application.
- **dynamodb_setup.py:** Python script for setting up the DynamoDB database.
- **Jenkinsfile:** Jenkins pipeline script for automating CI/CD processes.
- **requirements.txt:** File containing Python dependencies for the project.
- **templates:** Directory containing HTML templates for the Flask application.


## CI/CD Pipeline Steps:

1. **Setup DynamoDB:** Create a DynamoDB table using boto3 in a separate Python script.
2. **Build Docker Image:** Use Dockerfile to build a Docker image of the Flask application.
3. **Create ECR Repository:** Run a Python script to create an ECR repository for storing Docker images.
4. **Push Docker Image to ECR:** Push the built Docker image to the ECR repository.
5. **Create ECS Cluster:** Run a Python script to create an ECS cluster for deploying Docker containers.
6. **Deploy Flask Application to ECS:** Deploy the Docker container with the Flask application to the ECS cluster.
7. **Integrate SAST with Snyk:** Perform static application security testing using Snyk as part of the Jenkins pipeline.

## Getting Started:

1. **Clone the Repository:** Clone the project repository from GitHub.
2. **Install Dependencies:** Install Python dependencies listed in `requirements.txt`.
3. **Configure AWS Credentials:** Set up AWS credentials in Jenkins for accessing AWS services.
4. **Configure Jenkins Pipeline:** Create a new pipeline job in Jenkins and link it to the GitHub repository. Configure Jenkinsfile to define the CI/CD pipeline stages.
5. **Run the Pipeline:** Trigger the pipeline in Jenkins to build, test, and deploy the Flask application automatically.

By following these steps, we'll be able to deploy our Flask CRUD application seamlessly using a CI/CD pipeline managed by Jenkins.
