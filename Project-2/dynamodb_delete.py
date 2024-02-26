import boto3

def delete_dynamodb_table():
    dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
    table_name = 'Items'
    existing_tables = dynamodb.meta.client.list_tables()['TableNames']
    if table_name in existing_tables:
        table = dynamodb.Table(table_name)
        table.delete()
        table.wait_until_not_exists()

if __name__ == "__main__":
    delete_dynamodb_table()
