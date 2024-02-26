# dynamodb_setup.py

import boto3
import os

# Fetch the region name from the environment variable set by Jenkins
region_name = os.getenv('AWS_DEFAULT_REGION')

dynamodb = boto3.resource('dynamodb',region_name)

table_name = 'Items'
existing_tables = dynamodb.meta.client.list_tables()['TableNames']
if table_name not in existing_tables:
    # Create the DynamoDB table
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'  # Partition key
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'  # String type
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
        # Wait for the table to be created
    waiter = table.meta.client.get_waiter('table_exists')
    waiter.wait(TableName='Items')
    print(f"Table '{table.table_name}' created successfully.")
        
