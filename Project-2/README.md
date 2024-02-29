
# Jenkins-Project-2: Deploy a Login/Registration Website App Using CI/CD Pipeline in Jenkins to AWS ECS

## Project Introduction:
Welcome to our Login/Registration Website Application project! In this project, our goal is to develop a web application using Flask, a Python web framework, that allows users to register, log in, and manage their accounts. The main objective is to gain hands-on experience in building a web application, setting up a CI/CD pipeline using Jenkins, and deploying the application to AWS ECS (Elastic Container Service) for scalable and reliable execution.

## Objectives:
- **Develop a Login/Registration Website Application:** Create a Flask application that enables users to register, log in, and manage their accounts securely.
  
- **CI/CD Pipeline Setup:** Implement a Continuous Integration/Continuous Deployment (CI/CD) pipeline using Jenkins to automate the build, test, and deployment processes of the application.
  
- **Deployment to AWS ECS:** Deploy the Flask application to AWS ECS using Docker containers for containerized deployment and scalability.

## Tools and Technologies:
- **Flask:** Python web framework for building the application.
  
- **HTML/CSS:** Frontend markup and styling.
  
- **Jenkins:** CI/CD automation server for orchestrating the pipeline.
  
- **Docker:** Containerization technology for packaging the application.
  
- **AWS ECS:** Container orchestration service for deploying and managing Docker containers.
  
- **ECR (Elastic Container Registry):** Container registry service used to store Docker images.
  
- **Trivy:** Vulnerability scanner for container images, ensuring security compliance.

## Creating the Jenkins CI/CD Pipeline:
1. **GitHub Repository Setup:** Create a GitHub repository to host the project code, including the Flask application, Dockerfile, Jenkinsfile, and HTML templates.

2. **Jenkins Installation:** Install Jenkins on a server (could be an EC2 instance) and configure necessary plugins like Git, Docker, and AWS Pipeline.

3. **Jenkins Configuration:** Configure Jenkins credentials for accessing the GitHub repository, ECR, Docker Hub (or another container registry), and AWS services.

4. **Writing Jenkinsfile:** Define the CI/CD pipeline stages and steps in the Jenkinsfile. This includes checking out the code from GitHub, building the Docker image, pushing it to the container registry (ECR), scanning the image for security vulnerabilities using Trivy, and deploying to AWS ECS for Fargate execution.

5. **Pipeline Execution:** Create a new pipeline job in Jenkins and link it to the GitHub repository. Jenkins will automatically trigger the pipeline whenever changes are pushed to the repository.

## Deployment to AWS ECS:
1. **ECS Cluster Setup:** Configure an ECS cluster in AWS for deploying and managing Docker containers.

2. **Task Definition Definition:** Define a task definition for Fargate execution, specifying container image, CPU, memory, networking configuration, and other parameters.

3. **Deploying the Application:** Use the ECS service to deploy the Docker containers onto the ECS cluster, ensuring scalability and high availability.

By following these steps, we'll be able to create a robust CI/CD pipeline for our Login/Registration Website Application and deploy it seamlessly to AWS ECS environments for efficient and scalable execution.
