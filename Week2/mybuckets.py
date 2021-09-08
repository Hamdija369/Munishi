import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(F"Bucket: {bucket.name}")

my_bucket = s3.Bucket(bucket.name)

for file in my_bucket.objects.all():
    print(file.key)


