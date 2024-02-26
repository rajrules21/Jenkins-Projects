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
        clusterName=cluster_name
    )
    print("ECS Cluster created:", response['cluster']['clusterName'])

# 2. Register Task Definition for Fargate
def register_task_definition(task_family, container_image, cpu, memory):
    task_definition = {
        'family': task_family,
        'networkMode': 'awsvpc',  # Set network mode to awsvpc for Fargate
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
    response = ecs_client.register_task_definition(**task_definition)
    print("Task Definition registered:", response['taskDefinition']['taskDefinitionArn'])
    return response['taskDefinition']['taskDefinitionArn']

# 3. Create Task Definition
def create_task_definition(task_family, task_definition_arn):
    response = ecs_client.create_task_set(
        taskDefinition=task_definition_arn,
        cluster=cluster_name,
        service=service_name,
        launchType='FARGATE',  # Specify Fargate as the launch type
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': ['subnet-0796e98c324b7e10d'],  # Specify your subnet IDs
                'securityGroups': ['sg-04167ed144aefc3d8'],  # Specify your security group IDs
                'assignPublicIp': 'DISABLED'  # Specify 'ENABLED' if you want to assign public IP addresses
            }
        },
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

        # 2. Register Task Definition for Fargate
        task_definition_arn = register_task_definition(task_family, container_image, cpu, memory)

        # 3. Create Task Definition
        create_task_definition(task_family, task_definition_arn, cluster_name, service_name, desired_count)
    except Exception as e:
        print("An error occurred:", str(e))
        
if __name__ == "__main__":
    main()
