import boto3, csv

def Get_Instances(key,value):
    ec2_client = boto3.client('ec2')
    paginator = ec2_client.get_paginator('describe_instances')
    page_list = paginator.paginate(
       Filters=[
            {
                'Name':key,
                'Values':[value],
            },
         ]
    )
    response = []
    for page in page_list:
        for reservation in page['Reservations']:
            response.append(reservation)
#   response = ec2_client.describe_instances()
#   print(f"response: {response['Reservations']}")
    return response

def CSV_Writer(header,content):
    hFile = open('export.csv', 'w')
    writer = csv.DictWriter(hFile,fieldnames=header)
    writer.writeheader()
    for line in content:
        writer.writerow(line)
    hFile.close()

def main():
    reservations = Get_Instances('instance-state-name', 'running')
    header = ['InstanceId', 'InstanceType', 'State', 'PublicIpAddress', 'Monitoring', 'ImageId']
    content = []

    for instance in reservations:
        #print(f"Instance: {instance}")
        #print(f"Adding instance {instance['Instances'][0]['InstanceId']}")
        content.append(
            {
                "InstanceId": instance['Instances'][0]['InstanceId'],
                "InstanceType": instance['Instances'][0]['InstanceType'],
                "State": instance['Instances'][0]['State']['Name'],
                "PublicIpAddress": instance['Instances'][0].get('PublicIpAddress',"N/A"),
                "Monitoring": instance['Instances'][0]['Monitoring'],
                "ImageId":instance['Instances'][0]['ImageId'],
            }
        )
    CSV_Writer(header,content)

if __name__ == "__main__":
    main()