import boto3

s3 = boto3.client('s3')

BUCKET_NAME = "customer-churn-aws-lautaro"

LOCAL_FILE = "README.md"

S3_FILE = "README.md"

s3.upload_file(LOCAL_FILE, BUCKET_NAME, S3_FILE)

print("File uploaded successfully to S3 bucket.")