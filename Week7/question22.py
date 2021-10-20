import boto3
import argparse

def Get_Security_Groups():
    ec2_client = boto3.client('ec2')
    AllSecurityGroups = ec2_client.describe_security_groups()
    print()

ec2_client = boto3.client('ec2')
AllSecurityGroups = ec2_client.describe_security_groups()

ec2_client = boto3.client('ec2')
response = ec2_client.describe_security_groups(
    Filters=[
    {
        "Name": "ip-permission.cidr",
        "Values": [""]
    }
])
#print(response['SecurityGroups'])
for securitygroups in response['SecurityGroups']:
#    print(securitygroups)
#    print(f"The Follwoing Security Group is Open to The Public Internet! Group Name: {securitygroups['GroupName']}")
    print(f"It's Group Id is: {securitygroups['GroupId']}")
    for iprange in securitygroups['IpPermissions']:
        print(iprange)
        for cidr in iprange['IpRanges']:
            print
            print(f"Here is a description of it's IP Range: {cidr}")

#group_id = securitygroups['GroupId']