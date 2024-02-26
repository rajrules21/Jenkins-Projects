import sys
import boto3
import os

# Fetch the region name from the environment variable set by Jenkins
region_name = os.getenv('AWS_DEFAULT_REGION')

# Initialize ECS client
ecs_client = boto3.client('ecs')

# 1. Create an ECS Cluster
def create_ecs_cluster(region_name, cluster_name):
    response = ecs_client.create_cluster(
        clusterName=cluster_name)
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

# Main function
def main():
    try:
        # Extract command-line arguments
        aws_account_id = os.environ.get('AWS_ACCOUNT_ID')
        region_name = sys.argv[1]
        cluster_name = sys.argv[2]
        task_family = sys.argv[3]
        container_image = sys.argv[4]
        cpu = int(sys.argv[5])
        memory = int(sys.argv[6])
        service_name = sys.argv[7]
        desired_count = int(sys.argv[8])

        # 1. Create an ECS Cluster
        create_ecs_cluster(region_name, cluster_name)
        # 2. Define a Task Definition
        task_definition = define_task_definition(task_family, container_image, cpu, memory)

        # 3. Register Task Definition
        register_task_definition(task_definition)

        # 4. Create an ECS Service
        task_definition_arn = f"arn:aws:ecs:{region_name}:{aws_account_id}:task-definition/{task_family}"
        create_ecs_service(cluster_name, service_name, task_definition_arn, desired_count)
    except Exception as e:
        print("An error occurred:", str(e))
        
if __name__ == "__main__":
    main()
