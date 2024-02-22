# dynamodb_setup.py

import boto3

def create_dynamodb_table():
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
    table_name = 'Items'
    existing_tables = dynamodb.meta.client.list_tables()['TableNames']
    if table_name not in existing_tables:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'  # String
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.wait_until_exists()
