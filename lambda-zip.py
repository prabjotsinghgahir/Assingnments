import boto3
s = boto3.client('s3')
def handler(event, context):
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    dest_bucket_name = 'output-b-one'
    copy_object = {'Bucket':source_bucket, 'Key':file_name}
    s.copy_object(CopySource=copy_object,Bucket = dest_bucket_name,Key = file_name )
    print("Helooo fromm  me")