import boto3
client = boto3.client('s3')
bucket = client.list_objects(
    Bucket='week-2-task'
)
tag = input("Enter the file tag you want to delete:  ")
for i in bucket['Contents']:
    filename = i['Key']
    response = client.get_object_tagging(
        Bucket='week-2-task',
        Key=filename
    )
    #meta_data = client.
    tag_key = response['TagSet'][0]['Key']
    if(tag_key == tag):
        delete_file = client.delete_object(
            Bucket='week-2-task',
            Key=filename
        )
        print("File "+filename+"  is deleted  ")
    else:
        print("Not the same tag:  "+tag_key)
#print(len(bucket['Contents']))
