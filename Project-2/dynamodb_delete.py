import boto3
import os

# Fetch the region name from the environment variable set by Jenkins
region_name = os.getenv('AWS_DEFAULT_REGION')

dynamodb = boto3.resource('dynamodb', region_name)
table_name = 'Items'
existing_tables = dynamodb.meta.client.list_tables()['TableNames']
if table_name in existing_tables:
    table = dynamodb.Table(table_name)
    table.delete()
    table.wait_until_not_exists()
    print(f"Table '{table.table_name}' created successfully.")


