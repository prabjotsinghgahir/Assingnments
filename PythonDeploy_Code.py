import lambdafunctiondeploy
import boto3
import time

opening_temp = open("Week_1_final")
reading = opening_temp.read()
file_zip = 'lambda-zip.py'
lambda_code_bucket = 'codebucket-infy-lam'

client = boto3.client('cloudformation')

parameter = [
    {
        'ParameterKey': 'S3Bucketname',
        'ParameterValue': 'source-bucket-psg'
    },
    {
        'ParameterKey': 'S3Destbucket',
        'ParameterValue': 'destination-bucket-psg'
    },
    {
        'ParameterKey': 'LambdaCodeBucket',
        'ParameterValue': lambda_code_bucket
    }
]


class StackCreation():
    def create_stack(self):
        try:
            result = client.create_stack(
                StackName='assnig',
                TemplateBody=reading,
                Capabilities=['CAPABILITY_IAM'],
                Parameters=parameter
            )
        except client.exceptions.AlreadyExistsException as eror:
            print("Updating stack")
            try:
                client.update_stack(
                    StackName='assnig',
                    TemplateBody=reading,
                    # UsePreviousTemplate=True,
                    Capabilities=['CAPABILITY_IAM'],
                    Parameters=parameter
                )
            except client.exceptions.ClientError as err:
                print("Printing Error:  ", err)
            print("stack Updated")

    def stackstatus(self):
        response = client.describe_stacks(
            StackName='assnig'
        )
        res = response['Stacks'][0]['StackStatus']
        print(res)
        if (res == 'ROLLBACK_COMPLETE'):
            client.delete_stack(
                StackName='assnig'
            )
            print("Delete Complete")
        else:
            print("Template is created successfully")


lambdafunctiondeploy.ziper().zipping(file_zip)
print("Done calling zipper")
time.sleep(5)
lambdafunctiondeploy.LambdaFunction().lambdafunctionupload(lambda_code_bucket, file_zip)
print("Done calling lambda deployer")
time.sleep(10)
StackCreation().create_stack()
time.sleep(90)
StackCreation().stackstatus()
