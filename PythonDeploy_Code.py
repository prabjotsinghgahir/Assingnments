import boto3
sa = open("week_1")
sa1 = sa.read()
sl = boto3.client('cloudformation')
resul = sl.create_stack(
    StackName='assnig',
    TemplateBody=sa1,
    Capabilities = ['CAPABILITY_IAM']
)
