import lambdafunctiondeploy
import boto3
import time
opening_temp = open("Week_1_final")
reading = opening_temp.read()

client = boto3.client('cloudformation')

parameter = [
    {
        'ParameterKey': 'S3Bucketname',
        'ParameterValue':'source-bucket-psg'
    },
    {
        'ParameterKey': 'S3Destbucket',
        'ParameterValue': 'detination-bucket-psg'
    }
]

class stackcreation():
    def stack(self):
        try:
            result = client.create_stack(
                StackName='assnig',
                TemplateBody=reading,
                Capabilities = ['CAPABILITY_IAM'],
                Parameters= parameter
            )
        except client.exceptions.AlreadyExistsException:
            print("Udating stack")
            try:
                updatestack = client.update_stack(
                    StackName='assnig',
                    UsePreviousTemplate=True,
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
        if(res == 'ROLLBACK_COMPLETE'):
            deleting = client.delete_stack(
                StackName='assnig'
            )
            print("Delete Complete")
        else:
            print("Template is created successfully")

#lambdafunctiondeploy.ziper().zipping()
#print("Done calling zipper")
#time.sleep(5)
#lambdafunctiondeploy.lambdafunction().lambdafunctionupload()
#print("Done calling lambda deployer")
#time.sleep(10)
stackcreation().stack()
time.sleep(90)
stackcreation().stackstatus()
