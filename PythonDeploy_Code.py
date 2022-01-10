#import lambdafunctiondeploy
import boto3


client = boto3.client('cloudformation')


class StackCreation:
    def create_stack(self, stack_name, reading, parameter):
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

    def stackstatus(self, stack_name):
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