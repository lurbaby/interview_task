# Interview_task

## AWS 
## Creating s3 and adding files
![image](https://github.com/lurbaby/interview_task/assets/120603922/754ebf5d-928b-4c17-8da5-e7496ea52ff3)

## Adding IAM role to get access to s3
![image](https://github.com/lurbaby/interview_task/assets/120603922/04dec535-7aaf-4cbb-a9fd-f07c4c955ea4)

## List all s3 files
``` 
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
```

## Docker

## Writin' Dockerfile with pandas (multistage is not used for time reason) (pandas 1.26 not supported now latest using instead)
```
FROM python:3.10-slim

WORKDIR /usr/src/app

RUN pip install --upgrade pip && pip install pandas

CMD ["ls"]
```
## Building and running it in iteractive mode (-i)
```
docker build -t pandas-img .
docker run -it --name pandas-cont2 pandas-img bash
```
![image](https://github.com/lurbaby/interview_task/assets/120603922/f58ba1c0-2cc7-40a8-9962-dca035389384)


