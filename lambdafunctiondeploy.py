import boto3
import os
import shutil
cwd = os.getcwd()
file_to_zip = 'lambda-zip.py'
shutil.make_archive('lambda-zip','zip',cwd,file_to_zip)
lambda_upload = boto3.client('s3')
res = lambda_upload.upload_file('lambda-zip.zip', 'lambda-bucket-zip1', 'lambda-zip.zip')