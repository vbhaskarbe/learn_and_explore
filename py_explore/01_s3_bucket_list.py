##
## Author : Bhaskar Varadaraju
## A Python3 program to List buckets in AWS S3 
##
## ******  IMPORTANT : Set below before executing ******
##  export AWS_ACCESS_KEY_ID=<Your_Aws_KeyId>
##  export AWS_SECRET_ACCESS_KEY=<Your_Aws_Secret_Access_Key>
##

import boto3
# Retrieve the list of existing buckets
s3 = boto3.client('s3',
    region_name='ap-south-1',
)
response = s3.list_buckets()

# Output the bucket names in S3
print('INFO: List of buckets in S3:')
for s3bucket in response['Buckets']:
    print(f'  {s3bucket["Name"]}')

