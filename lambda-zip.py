import boto3
import os
s = boto3.client('s3')


def handler(event, context):
    destination_bucket = os.getenv('takeBucket')
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    copy_object = {'Bucket': source_bucket, 'Key': file_name}
    s.copy_object(CopySource=copy_object, Bucket=destination_bucket, Key=file_name)
    print("Helooo fromm  me")
