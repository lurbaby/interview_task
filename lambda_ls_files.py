import json
import boto3

def lambda_handler(event, context):
    
    bucket = "test-task-bucket123"
    s3 = boto3.client("s3")
    
    try:
        data = []
    
        for item in s3.list_objects(Bucket=bucket)["Contents"]:
            data.append(item["Key"])

        return {
            'statusCode': 200,
            'body': data
        }
    
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
        
    
    

