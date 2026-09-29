import boto3

def import_data():
    s3_client = boto3.client('s3')
    s3_resource = boto3.resource('s3')

    # checking what key to refer to to download csv file
    response = s3_client.list_objects_v2(Bucket='la-metro-bike-share-2020-2025')
    objects = response.get('Contents', [])

    s3_client.download_file(Bucket='la-metro-bike-share-2020-2025', Key='queries/to_python/2026/09/28/34733e41-e3bf-4d67-aea9-565b3442e10d.csv', Filename='to_python.csv')