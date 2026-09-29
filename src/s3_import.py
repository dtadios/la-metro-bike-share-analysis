import boto3

def import_data():
    s3_client = boto3.client('s3')
    s3_resource = boto3.resource('s3')

    # checking what key to refer to to download csv file
    response = s3_client.list_objects_v2(Bucket='la-metro-bike-queries')
    objects = response.get('Contents', [])

    s3_client.download_file(Bucket='la-metro-bike-queries', Key='rental_bike_data/2026/09/26/c041f76d-c150-43b3-95a2-53f5eb1d950d.csv', Filename='rental_bike_data.csv')
