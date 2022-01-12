import PythonDeploy_Code
import lambdafunctiondeploy


template_name = 'Week_1_final'
file_zip = 'lambda-zip.py'
lambda_code_bucket = 'code-bucket-psg'
stack_name = 'assignment1'
source_bucket_name = 'source-bucket-psg'
destination_bucket_name = 'destination-bucket-psg'
region = 'ap-south-1'


parameter = [
        {
            'ParameterKey': 'S3BucketName',
            'ParameterValue': source_bucket_name
        },
        {
            'ParameterKey': 'S3DestinationBucket',
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


opening_temp = open(template_name)
reading = opening_temp.read()

call_class_lambda = lambdafunctiondeploy.ZipAndUploadLambda(file_zip, lambda_code_bucket, region)
call_create_stack = PythonDeploy_Code.StackCreation(stack_name, reading, parameter)

call_class_lambda.zipping()
print("Done calling zipper")
call_class_lambda.lambda_function_upload()
print("Done calling lambda deployer")
call_create_stack.create_stack()
call_create_stack.stack_status()
