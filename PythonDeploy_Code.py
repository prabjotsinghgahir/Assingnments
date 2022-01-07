import lambdafunctiondeploy
import boto3


opening_temp = open("Week_1_final")
reading = opening_temp.read()
file_zip = 'lambda-zip.py'
lambda_code_bucket = 'codebucket-infy-lam'
stackname = 'assnig'

client = boto3.client('cloudformation')

parameter = [
    {
        'ParameterKey': 'S3Bucketname',
        'ParameterValue': 'source-bucket-psg'
    },
    {
        'ParameterKey': 'S3Destbucket',
        'ParameterValue': 'desti-bucket-psg'
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
                StackName=stackname,
                TemplateBody=reading,
                Capabilities=['CAPABILITY_IAM'],
                Parameters=parameter
            )
            print("Creating Stack")
            waiter = client.get_waiter('stack_create_complete')
            waiter.wait(StackName=stackname)
            print("Stack Created")
        except client.exceptions.AlreadyExistsException as eror:
            print("Updating stack")
            try:
                client.update_stack(
                    StackName=stackname,
                    TemplateBody=reading,
                    # UsePreviousTemplate=True,
                    Capabilities=['CAPABILITY_IAM'],
                    Parameters=parameter
                )
                waiter = client.get_waiter('stack_update_complete')
                waiter.wait(StackName=stackname)
            except client.exceptions.ClientError as err:
                print("Printing Error:  ", err)
            print("stack Updated")

    def stackstatus(self):
        response = client.describe_stacks(
            StackName=stackname
        )
        res = response['Stacks'][0]['StackStatus']
        print(res)
        if res == 'ROLLBACK_COMPLETE':
            client.delete_stack(
                StackName=stackname
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
