import PythonDeploy_Code
import lambdafunctiondeploy


def call_para():
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
                'ParameterValue': file_zip.split('.')[0] + ".zip"
            },
            {
                'ParameterKey': 'LambdaHandler',
                'ParameterValue': file_zip.split('.')[0] + ".handler"
            }
        ]
    return parameter


a = int(input("Enter how many templates to deploy:  "))

for i in range(0, a):
    template_name = input("Enter the template name:  ")
    opening_temp = open(template_name)
    reading = opening_temp.read()
    file_zip = input("Enter lambda function file name:  ")
    lambda_code_bucket = input("Enter lambda code bucket name:  ")
    stack_name = input("Enter stack name:  ")
    source_bucket_name = input("Enter Source bucket name:  ")
    destination_bucket_name = input("Enter Destination bucket name:  ")
    lambdafunctiondeploy.ziper().zipping(file_zip)
    print("Done calling zipper")
    lambdafunctiondeploy.LambdaFunction().lambdafunctionupload(lambda_code_bucket, file_zip)
    print("Done calling lambda deployer")
    PythonDeploy_Code.StackCreation().create_stack(stack_name, reading, call_para())
    PythonDeploy_Code.StackCreation().stackstatus(stack_name)

'''parameter = [
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
]'''



'''opening_temp = open("Week_1_final")
reading = opening_temp.read()
file_zip = 'lambda-zip.py'
lambda_code_bucket = 'codebucket-infy-lam'
stack_name = 'assnig'
source_bucket_name = 'source-bucket-psg'
destination_bucket_name = 'desti-bucket-psg'''