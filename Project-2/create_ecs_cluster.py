import boto3
import os
import sys

# Initialize ECS client
ecs_client = boto3.client("ecs", region_name="ap-south-1")



# 1. Create an ECS Cluster
def create_ecs_cluster(region_name, cluster_name):
    response = ecs_client.create_cluster(
        clusterName=cluster_name
    )
    cluster_name = response['cluster']['clusterName']  # Assign the returned cluster name
    print("ECS Cluster created:", cluster_name)
    return cluster_name  # Return the cluster name

# 2. Define a Task Definition for Fargate
def define_task_definition(task_family, container_image, cpu, memory):
    print("CPU value:", cpu)
    response = ecs_client.register_task_definition(
        containerDefinitions=[
            {
                "name": task_family,
                "image": container_image,
                "cpu": cpu,
                "memory": memory,
                "essential": True,
                "portMappings": [
                    {
                        "containerPort": 5000,
                        "hostPort": 5000,
                        "protocol": "tcp"
                    }
                ],                
            }
        ],
        family=task_family,
        cpu="1024",
        memory="2048",
        networkMode="awsvpc",
        requiresCompatibilities=["FARGATE"],
        runtimePlatform={
            "cpuArchitecture": "X86_64",
            "operatingSystemFamily": "LINUX"
        },
        executionRoleArn="arn:aws:iam::811172515558:role/AmazonSSMRoleForInstancesQuickSetup"
    )
    print("Task Definition registered:", response['taskDefinition']['taskDefinitionArn'])
    return response['taskDefinition']['taskDefinitionArn']

# 3. Create an ECS Service for Fargate
def create_ecs_service(cluster_name, service_name, task_definition_arn, desired_count):
    response = ecs_client.create_service(
        cluster=cluster_name,
        serviceName=service_name,
        taskDefinition=task_definition_arn,
        desiredCount=desired_count,
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': ['subnet-0796e98c324b7e10d'],  # Specify your subnet IDs
                'securityGroups': ['sg-04167ed144aefc3d8'],  # Specify your security group IDs
                'assignPublicIp': 'ENABLED'  # Specify 'ENABLED' if you want to assign public IP addresses
            }
        },
        launchType="FARGATE"  # Specify Fargate as the launch type
    )
    print("ECS Service created:", response['service']['serviceName'])
    return response['service']['serviceName']

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
        cluster_name = create_ecs_cluster(region_name, "my-ecs-name")

        # 2. Define a Task Definition for Fargate
        task_definition_arn = define_task_definition(task_family, container_image, cpu, memory)

        # 3. Create an ECS Service for Fargate
        create_ecs_service(cluster_name, service_name, task_definition_arn, desired_count)
    except Exception as e:
        print("An error occurred:", str(e))
        
if __name__ == "__main__":
    main()
