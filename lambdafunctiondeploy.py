import boto3
import os
import shutil


class ziper:
    def zipping(self, file_zip):
        cwd = os.getcwd() + "\lambda_zips"
        file_to_zip = file_zip.split('.')
        shutil.make_archive(file_to_zip[0], 'zip', cwd, file_zip)


class LambdaFunction:
    def lambdafunctionupload(self, lambda_code_bucket, file_zip):
        lambda_upload = boto3.client('s3')
        try:
            lambda_upload.create_bucket(
                Bucket=lambda_code_bucket,
                CreateBucketConfiguration={
                    'LocationConstraint': 'ap-south-1'
                },
            )
        except lambda_upload.exceptions.BucketAlreadyOwnedByYou:
            pass
        file_zip = file_zip.split('.')
        file_zip_one = file_zip[0] + ".zip"
        lambda_upload.upload_file(file_zip_one, lambda_code_bucket, file_zip_one)


