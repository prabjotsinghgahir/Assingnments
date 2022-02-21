import boto3
from botocore.exceptions import WaiterError

client = boto3.client('cloudformation')


class StackCreation:
    def __init__(self, stack_name, reading, parameter):
        self.stack_name = stack_name
        self.reading = reading
        self.parameter = parameter

    def create_stack(self):
        try:
            client.create_stack(
                StackName=self.stack_name,
                TemplateBody=self.reading,
                Capabilities=['CAPABILITY_IAM'],
                Parameters=self.parameter
            )
            print("Creating Stack")
            waiter = client.get_waiter('stack_create_complete')
            waiter.wait(StackName=self.stack_name)
            print("Stack Created")
        except WaiterError:
            pass
        except client.exceptions.AlreadyExistsException:
            print("Updating stack")
            try:
                client.update_stack(
                    StackName=self.stack_name,
                    TemplateBody=self.reading,
                    Capabilities=['CAPABILITY_IAM'],
                    Parameters=self.parameter
                )
                waiter = client.get_waiter('stack_update_complete')
                waiter.wait(StackName=self.stack_name)
            except WaiterError:
                pass
            except client.exceptions.ClientError as err:
                print("Printing Error:  ", err)
            print("stack Updated")

    def stack_status(self):
        response = client.describe_stacks(
            StackName=self.stack_name
        )
        res = response['Stacks'][0]['StackStatus']
        print(res)
        if res == 'ROLLBACK_COMPLETE':
            stack_events = client.describe_stack_events(StackName=self.stack_name)['StackEvents']
            for i in stack_events:
                try:
                    print(i['LogicalResourceId'], end=" ")
                    print(i['ResourceType'], end="  ")
                    print(i['ResourceStatus'], end="  ")
                    print(i['ResourceStatusReason'])
                except KeyError:
                    pass
            client.delete_stack(
                StackName=self.stack_name
            )
            print("Delete Complete")
        else:
            print("Template is created successfully")
