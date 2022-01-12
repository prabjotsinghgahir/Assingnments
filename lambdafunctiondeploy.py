import boto3
import os
import shutil


class ZipAndUploadLambda:
    def __init__(self, file_zip, lambda_code_bucket, region):
        self.file_zip = file_zip
        self.lambda_code_bucket = lambda_code_bucket
        self.region = region

    def zipping(self):
        cwd = os.getcwd()
        ced = os.path.join(cwd, 'lambda_zips')
        file_to_zip = self.file_zip.split('.')[0]
        ced = os.path.join(ced, file_to_zip)
        shutil.make_archive(ced, 'zip', cwd, self.file_zip)

    def lambda_function_upload(self):
        lambda_upload = boto3.client('s3')
        try:
            lambda_upload.create_bucket(
                Bucket=self.lambda_code_bucket,
                CreateBucketConfiguration={
                    'LocationConstraint': self.region
                },
            )
        except lambda_upload.exceptions.BucketAlreadyOwnedByYou:
            pass
        # file_zip = file_zip.split('.')
        cwd = os.path.join(os.getcwd(), 'lambda_zips')
        file_zip_one = self.file_zip.split('.')[0] + ".zip"
        cwd = os.path.join(cwd, file_zip_one)
        lambda_upload.upload_file(cwd, self.lambda_code_bucket, file_zip_one)
