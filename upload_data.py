import requests
import boto3
import json

# Fetch horoscope data from the API
url = "https://zylalabs.com/api/891/horoscope+api/694/get+horoscope?day=week&sunsign=pisces"
headers = {
    'Authorization': 'Bearer 1845|vdm1T1BQIue4h63obNgLoEJOVH5XSCa4KZgiXSwS'
}
response = requests.get(url, headers=headers)
horoscope_data = response.json()

# Initialize S3 client (ensure you've configured your AWS credentials)
s3 = boto3.client('s3')

# Bucket name and object key for storing the horoscope data
s3_bucket_name = 'horodata1'
object_key = 'horoscopes/pisces_weekly.json'

# Upload JSON data to S3
try:
    s3.put_object(Body=json.dumps(horoscope_data), Bucket=s3_bucket_name, Key=object_key)
    print(f'Successfully uploaded {object_key} to {s3_bucket_name}')
except Exception as e:
    print(f'Error uploading {object_key} to {s3_bucket_name}: {str(e)}')
