import boto3

def create_ecr_repository(repository_name):
    """
    Create an ECR repository with the given name.

    Args:
    - repository_name: The name of the ECR repository to create.

    Returns:
    - The ARN of the created repository if successful, None otherwise.
    """
    try:
        ecr_client = boto3.client('ecr')
        response = ecr_client.create_repository(repositoryName=repository_name,tags=[
        {
            'Key': 'image',
            'Value': 'flask-crud-app'
        }])
        repository_arn = response['repository']['repositoryArn']
        print(f"ECR repository '{repository_name}' created successfully.")
        return repository_arn
    except Exception as e:
        print(f"An error occurred while creating ECR repository '{repository_name}': {e}")
        return None

if __name__ == "__main__":
    repository_name = "flask-crud-image-repo"  # Replace with your desired repository name
    repository_arn = create_ecr_repository(repository_name)
    if repository_arn:
        print(f"Repository ARN: {repository_arn}")
    else:
        print("Failed to create repository.")
