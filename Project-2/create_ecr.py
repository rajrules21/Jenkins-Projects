import boto3
import os

def create_ecr_repository(repository_name, region_name):
    try:
        # Create a Boto3 client for ECR in the specified region
        ecr_client = boto3.client('ecr', region_name=region_name)

        # Create the ECR repository
        response = ecr_client.create_repository(
            repositoryName=repository_name,
            tags=[
                {
                    'Key': 'image',
                    'Value': 'flask-crud-app'
                }
            ]
        )
        
        repository_arn = response['repository']['repositoryArn']
        print(f"ECR repository '{repository_name}' created successfully.")
        return repository_arn
    except Exception as e:
        print(f"An error occurred while creating ECR repository '{repository_name}': {e}")
        return None

if __name__ == "__main__":
    repository_name = "flask-crud-image-repo"  # Replace with your desired repository name
    
    # Get the region name from the environment variable
    region_name = os.getenv('AWS_DEFAULT_REGION')
    
    # Call the function to create the ECR repository
    repository_arn = create_ecr_repository(repository_name, region_name)
    
    if repository_arn:
        print(f"Repository ARN: {repository_arn}")
    else:
        print("Failed to create repository.")