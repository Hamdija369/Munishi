import boto3
import json, argparse
import string, random
import botocore

s3 = boto3.client('s3')

bucket_name = 'week2-bucket-hamdija369-ex2'

parser = argparse.ArgumentParser(description='This is to allow arguments for my s3website script')

parser.add_argument('-s','--site-name', dest='site_name', default='', type=str,help='Enter a unique bucket name')

args = parser.parse_args()
print(args.site_name)
if not args.site_name:
    print(f"No site-name provided, using our random generator")
    bucket_name += "".join(random.choices(string.ascii_lowercase, k=10))
else:
    bucket_name = args.site_name
try:
    response = s3.create_bucket(Bucket=bucket_name)
    #print(response)

    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{ 
            'Sid': 'AddPerm', 
            'Effect': 'Allow', 
            'Principal': '*', 
            'Action': ['s3:GetObject'], 
            'Resource': "arn:aws:s3:::%s/*" % bucket_name
            }] 
    } 
    bucket_policy = json.dumps(bucket_policy, indent=4)
    #print(bucket_policy

    policy_response = s3.put_bucket_policy(Bucket=bucket_name,Policy=bucket_policy)
    print(policy_response)

    website_response = s3.put_bucket_website(
        Bucket=bucket_name,
        WebsiteConfiguration={
            'ErrorDocument': {'Key': 'error.html'},
            'IndexDocument': {'Suffix': 'index.html'},
        }
    )
    print(website_response)

    index_file = open('index.html', 'rb')
    response = s3.put_object(Body=index_file,Bucket=bucket_name,Key='index.html', ContentType='text/html')
    index_file.close()
    print(response)

    error_file = open('error.html', 'rb')
    response = s3.put_object(Body=error_file,Bucket=bucket_name,Key='error.html', ContentType='text/html')
    print(response)

except botocore.exceptions.ClientError as error:
#    print(error)
    if error.response['Error']['Code'] == 'InvalidToken':
        print("Please update your AWS Credentials with a valid token")
    else:
        print(f"Some other error occured {error}")

