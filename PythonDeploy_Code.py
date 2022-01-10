import lambdafunctiondeploy
import boto3


opening_temp = open("Week_1_final")
reading = opening_temp.read()
file_zip = 'lambda-zip.py'
lambda_code_bucket = 'codebucket-infy-lam'
stack_name = 'assnig'
source_bucket_name = 'source-bucket-psg'
destination_bucket_name = 'desti-bucket-psg'

client = boto3.client('cloudformation')

parameter = [
    {
        'ParameterKey': 'S3Bucketname',
        'ParameterValue': source_bucket_name
    },
    {
        'ParameterKey': 'S3Destbucket',
        'ParameterValue': destination_bucket_name
    },
    {
        'ParameterKey': 'LambdaCodeBucket',
        'ParameterValue': lambda_code_bucket
    },
    {
        'ParameterKey': 'LambdaKey',
        'ParameterValue': file_zip.split('.')[0]+".zip"
    },
    {
        'ParameterKey': 'LambdaHandler',
        'ParameterValue': file_zip.split('.')[0]+".handler"
    }
]


class StackCreation():
    def create_stack(self):
        try:
            client.create_stack(
                StackName=stack_name,
                TemplateBody=reading,
                Capabilities=['CAPABILITY_IAM'],
                Parameters=parameter
            )
            print("Creating Stack")
            waiter = client.get_waiter('stack_create_complete')
            waiter.wait(StackName=stack_name)
            print("Stack Created")
        except client.exceptions.AlreadyExistsException as eror:
            print("Updating stack")
            try:
                client.update_stack(
                    StackName=stack_name,
                    TemplateBody=reading,
                    # UsePreviousTemplate=True,
                    Capabilities=['CAPABILITY_IAM'],
                    Parameters=parameter
                )
                waiter = client.get_waiter('stack_update_complete')
                waiter.wait(StackName=stack_name)
            except client.exceptions.ClientError as err:
                print("Printing Error:  ", err)
            print("stack Updated")

    def stackstatus(self):
        response = client.describe_stacks(
            StackName=stack_name
        )
        res = response['Stacks'][0]['StackStatus']
        print(res)
        if res == 'ROLLBACK_COMPLETE':
            client.delete_stack(
                StackName=stack_name
            )
            print("Delete Complete")
        else:
            print("Template is created successfully")


lambdafunctiondeploy.ziper().zipping(file_zip)
print("Done calling zipper")
lambdafunctiondeploy.LambdaFunction().lambdafunctionupload(lambda_code_bucket, file_zip)
print("Done calling lambda deployer")
StackCreation().create_stack()
StackCreation().stackstatus()
