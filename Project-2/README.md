# Jenkins-Project-2: Deploy a Python Flask CRUD App Using CI/CD Pipeline in Jenkins

## Project Introduction:

Welcome to our Simple Flask CRUD Application  project! In this project, we aim to develop a crud application using Flask, a lightweight Python web framework, to manage crud functionality in a DynamoDB Table. The main objective of this project is to provide hands-on experience with building a web application, setting up a CI/CD pipeline using Jenkins, and deploying the application to AWS AWS ECS.

## Objectives:

- **Develop a Simple Flask CRUD Application:** Create a Flask application that allows users to perform create, read, update and delete operations on a DynamoDB table.

- **Create a DynamoDB Table:** write a python script to create a dynamodb tab;e
  
- **CI/CD Pipeline Setup:** Implement a Continuous Integration/Continuous Deployment (CI/CD) pipeline using Jenkins to automate the build, test, and deployment processes of the application.
  
- **Deployment to AWS EC2:** Deploy the Flask application to an AWS EC2 instance using Docker containers.

## Tools and Technologies:

- **Flask:** Python web framework for building the application.
- **HTML/CSS:** Frontend markup and styling.
- **Jenkins:** CI/CD automation server for orchestrating the pipeline.
- **Docker:** Containerization technology for packaging the application.
- **AWS EC2:** Virtual server instances for hosting the application.

## Creating the Jenkins CI/CD Pipeline:

- **GitHub Repository Setup:** Create a GitHub repository to host the project code, including the Flask application, Dockerfile, Jenkinsfile, and HTML templates.
  
- **Jenkins Installation:** Install Jenkins on a server (could be an EC2 instance) and set up necessary plugins like Git, Docker, and AWS Pipeline.
  
- **Jenkins Configuration:** Configure Jenkins credentials for accessing the GitHub repository, Docker Hub (or another container registry), and AWS services.
  
- **Writing Jenkinsfile:** Define the CI/CD pipeline stages and steps in the Jenkinsfile. This includes checking out the code from GitHub, building the Docker image, pushing it to the container registry, deploying to AWS EC2, and deploying to AWS ECS.
  
- **Pipeline Execution:** Create a new pipeline job in Jenkins and link it to the GitHub repository. Jenkins will automatically trigger the pipeline whenever changes are pushed to the repository.

## Deployment to AWS EC2:

- **EC2 Instance Setup:** Launch an EC2 instance and configure it with Docker to run Docker containers.
  
- **Deploying the Application:** Use SSH to connect to the EC2 instance from Jenkins and pull the Docker image. Run the Docker container to deploy the Flask application.

By following these steps, we'll be able to create a robust CI/CD pipeline for our Flask application and deploy it seamlessly to AWS EC2  environments.
