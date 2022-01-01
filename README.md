# Assingnments
1)PythonDeploy_code.py:
  This file is the main file which deploy everything on aws. This basically creates a stack of file "Week_1_final" and deploy it on aws. Then it monitors the status of stack.
  If the status is CREATION_COMPLETE then it prints "template is created succesfully" and if the status is ROLLBACK_COMPLETE then it deletes the stack and also the bucket which
  contains lambdafunction zip file.

2)lambdafunctiondeploy.py:
  This file first zips the lambda function file(lambda-zip.py) and store it in local directory. Then it creates a new s3 bucket and upload the zip lambda function file(lambda-zip.zip)
  on that new bucket. Basically it zips the lambdafunction and upload it in s3 bucket.
 
3)lambda-zip.py:
  It is the lambda function. This program do the copy and paste operation i.e it copies the file from the source s3 bucket and paste\put it in destination bucket.

4)Week_1_final:
  This is a cloudformation template. It is in a .yaml extention format. This template creates 5 aws resources i.e Two s3 buckets, lambdapermission , lambdafunction , IAM role.
  When an object is created in source s3 bucket it will trigger the lambda function. The lambda function will copy that object from source s3 bucket and will put it in
  destination s3 bucket. This template will perform the above task.  
