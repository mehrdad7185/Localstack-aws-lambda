import json
import os
import boto3
import uuid

# Initialize the DynamoDB resource

dynamodb = boto3.resource('dynamodb')

# Get the table name from Environment Variables set in Terraform
table_name = os.environ.get('TABLE_NAME')
table = dynamodb.Table(table_name)

def handler(event, context):
    """
    This function is triggered by API Gateway.
    It receives a JSON body, saves it to DynamoDB, and returns a success message.
    """
    
    print("Received Event:", json.dumps(event))

    # 1. Parse the incoming JSON body
    # API Gateway sends the data in the 'body' field as a string
    try:
        body = json.loads(event.get('body', '{}'))
    except:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid JSON body"})
        }

    student_name = body.get('name')
    student_major = body.get('major')

    if not student_name:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing 'name' field"})
        }

    # 2. Create a unique ID
    student_id = str(uuid.uuid4())

    # 3. Save to DynamoDB
    try:
        table.put_item(
            Item={
                'student_id': student_id,
                'name': student_name,
                'major': student_major,
                'status': 'Enrolled'
            }
        )
        print(f"Saved student {student_name} to DB.")
    except Exception as e:
        print("DynamoDB Error:", e)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Could not save to database"})
        }

    # 4. Return success response to the client
    return {
        "statusCode": 201,
        "body": json.dumps({
            "message": "Student registered successfully!",
            "student_id": student_id,
            "name": student_name
        })
    }
