import boto3
import sys
import os

def fetch_and_delete_ecr(repository_name, region_name):
    try:
        # Create a Boto3 client for ECR in the specified region
        ecr_client = boto3.client('ecr', region_name=region_name)

        # Describe the repository to get its ARN
        response = ecr_client.describe_repositories(repositoryNames=[repository_name])

        if 'repositories' in response and response['repositories']:
            # If repository exists, delete it
            ecr_client.delete_repository(repositoryName=repository_name, force=True)
            print(f"ECR repository '{repository_name}' deleted successfully.")
        else:
            print(f"ECR repository '{repository_name}' not found.")

    except Exception as e:
        print(f"An error occurred while deleting ECR repository '{repository_name}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    repository_name = "flask-crud-image-repo"  # Repository name passed as command-line argument
    region_name = os.getenv('AWS_DEFAULT_REGION')  # AWS region name passed as command-line argument

    # Call the function to fetch and delete the ECR repository
    fetch_and_delete_ecr(repository_name, region_name)
