import boto3
import time


ENDPOINT_URL = "http://localhost:4566"

def create_resources():
    
    dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url=ENDPOINT_URL,
        region_name='us-east-1',
        aws_access_key_id='test',      
        aws_secret_access_key='test'   
    )

    print("creating DynamoDB...")
    
    try:
        table = dynamodb.create_table(
            TableName='Students',
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'}  # Primary Key
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'}
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print("waiting for creating tables...")
        table.wait_until_exists()
        print("students table created!")
        
    except Exception as e:
        print(f"failed creating table: {e}")

if __name__ == "__main__":
    create_resources()
