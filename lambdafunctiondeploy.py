import boto3
import os
import shutil
class ziper():
    def zipping(self):
        cwd = os.getcwd()
        file_to_zip = 'lambda-zip.py'
        shutil.make_archive('lambda-zip','zip',cwd,file_to_zip)
class ld():
    def lc(self):
        lambda_upload = boto3.client('s3')
        bucket_code = lambda_upload.create_bucket(
            Bucket='codebucket-infy-lam',
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-south-1'
            },
        )
        res = lambda_upload.upload_file('lambda-zip.zip', 'codebucket-infy-lam', 'lambda-zip.zip')