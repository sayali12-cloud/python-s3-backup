""" 
This is a script to take a abackup from local to AWS S3
"""

import boto3

s3 = boto3.resource("s3")

def show_bucket(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_bucket(s3,bucket_name,region):
    s3.create_bucket(Bucket=bucket_name,
                      CreateBucketConfiguration={
                    'LocationConstraint': region,
                      },)
    print("bucket create successfully")

create_bucket(s3)

show_bucket(s3)

def upload_backup(s3,file_name,bucket_name,key_name):
    """
      Upload a given backup file path to a given s3 bucket with a new name(key)
    """
    data = open(file_name,'rb')  # file gets read in binary 
    s3.Bucket(bucket_name).put_object(Key=key_name,Body=data)
    print("Backup Upload Successfully") 
    
bucket_name = "python-bucket-for-devops1"
region = "ap-south-1"
file_name = "C:/Users/admin/Documents/python-for-devops/backups/backup_2026-03-06.tar.gz"
upload_backup(s3,file_name,bucket_name,"my-backup.tar.gz") # calling function

