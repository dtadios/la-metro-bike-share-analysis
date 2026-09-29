import boto3
import process

def upload_to_s3(csv_file):
    s3_client = boto3.client('s3')

    # uploading to s3 bucket
    
    bucket_name = 'la-metro-bike-share-2020-2025'
    subfolder_path = 'queries/final/'
    file_name = csv_file
    object_key = f"{subfolder_path}{file_name}"

    s3_client.upload_file(file_name, bucket_name, object_key)