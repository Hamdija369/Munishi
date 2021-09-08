import boto3
import json
import datetime

def defaultconverter(o):
    if isinstance (o, datetime.datetime):
        return o.__str__()

s3 = boto3.client('s3')

#print(type(s3))

response = s3.list_buckets()

format_response = json.dumps(response, default=defaultconverter, indent=4)

for bucket in response['Buckets']:
    print(bucket['Name'])

