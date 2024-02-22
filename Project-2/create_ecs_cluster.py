import boto3

# Initialize ECS client
ecs_client = boto3.client('ecs')

# 1. Create an ECS Cluster
def create_ecs_cluster(cluster_name):
    response = ecs_client.create_cluster(
        clusterName=cluster_name
    )
    print("ECS Cluster created:", response['cluster']['clusterName'])

# 2. Define a Task Definition
def define_task_definition(task_family, container_image, cpu, memory):
    task_definition = {
        'family': task_family,
        'containerDefinitions': [
            {
                'name': task_family,
                'image': container_image,
                'cpu': cpu,
                'memory': memory,
                'essential': True,
                # Add more container configuration as needed
            },
        ],
    }
    return task_definition

# 3. Register Task Definition
def register_task_definition(task_definition):
    response = ecs_client.register_task_definition(**task_definition)
    print("Task Definition registered:", response['taskDefinition']['taskDefinitionArn'])

# 4. Create an ECS Service
def create_ecs_service(cluster_name, service_name, task_definition_arn, desired_count):
    response = ecs_client.create_service(
        cluster=cluster_name,
        serviceName=service_name,
        taskDefinition=task_definition_arn,
        desiredCount=desired_count,
    )
    print("ECS Service created:", response['service']['serviceName'])

# Example usage
if __name__ == "__main__":
    # Replace these values with your specific configuration
    cluster_name = 'my-cluster'
    task_family = 'my-task-family'
    container_image = 'your-docker-image-url'
    cpu = '256'  # CPU units
    memory = '512'  # Memory in MB
    service_name = 'my-service'
    desired_count = 1

    # 1. Create an ECS Cluster
    create_ecs_cluster(cluster_name)

    # 2. Define a Task Definition
    task_definition = define_task_definition(task_family, container_image, cpu, memory)

    # 3. Register Task Definition
    register_task_definition(task_definition)

    # 4. Create an ECS Service
    task_definition_arn = f"arn:aws:ecs:REGION:ACCOUNT_ID:task-definition/{task_family}"
    create_ecs_service(cluster_name, service_name, task_definition_arn, desired_count)
