import boto3
bucketname = 'week-2-task'
client = boto3.client('s3')
bucket = client.list_objects(
    Bucket=bucketname
)
class deletetag():
    def deletewithtag(self):
        tag = input("Enter the file tag Value you want to delete:  ")
        try:
            for i in bucket['Contents']:
                filename = i['Key']
                response = client.get_object_tagging(
                    Bucket=bucketname,
                    Key=filename
                )
                tag_value = response['TagSet'][0]['Value']
                print(tag_value)
                if(tag_value == tag):
                    delete_file = client.delete_object(
                        Bucket=bucketname,
                        Key=filename
                    )
                    print("File "+filename+" with the above tag value is deleted  ")
                else:
                    print("No file found with this tag value:  " + tag)
        except KeyError as error:
            print("No key has the above typed value:  "+tag)
    #print(len(bucket['Contents']))
    def deletewithmetadta(self):
        #common = 'x-amz-meta-'
        #keyname = input("Enter the key name for meta data:  ")
        value = input("Enter the value of the object you want to delete:  ")
        #final = common + keyname
        try:
            for j in bucket['Contents']:
                filename = j['Key']
                metadata = client.head_object(
                    Bucket = bucketname,
                    Key = filename
                )
                #metavalue = metadata['ResponseMetadata']['HTTPHeaders'][final]
                metatag, metavalue = next(iter(metadata['Metadata'].items()))
                print(metavalue)
                print(metatag)
                '''if(metavalue == value):
                    print("Succsess value:  "+metavalue+"  and Key: "+value)
                else:
                    print("Not expected")'''
                if (value == metavalue):
                    client.delete_object(
                        Bucket = bucketname,
                        Key = filename
                    )
                    print("deleted succesfully:  "+filename)
                else:
                    print("Not deleted")
        except KeyError as err:
            print("The Following key is not present try another:  ",err)

deletetag().deletewithtag()

deletetag().deletewithmetadta()