import boto3
import argparse

ec2_client = boto3.client('ec2')
AllSecurityGroups = ec2_client.describe_security_groups()

ec2_client = boto3.client('ec2')
response = ec2_client.describe_security_groups(
    Filters=[
    {
        "Name": "ip-permission.cidr",
        "Values": ["0.0.0.0/0"]
    }
])
#print(response['SecurityGroups'])
for securitygroups in response['SecurityGroups']:
    for iprange in securitygroups['IpPermissions']:
        for cidr in iprange['IpRanges']:
            print

group_id = securitygroups['GroupId']

parser = argparse.ArgumentParser(description='This is to allow a user to input a security group name. ')
parser.add_argument('-sg','--group-id', default='', help='Enter a Secuirty Group ID')
args = parser.parse_args()
print(f"You have asked about the following Security Group: {args.group_id}")
if args.group_id != securitygroups['GroupId']:
    print(f'The Security Group you are Inquiring About is NOT open to the Internet!!!')
if not args.group_id:
    print(f"No Security Group ID Given --- After typing the command Python3 ec2-sg.py -- type -sg followed with the security group name. \n\nOtherwise here is a list of this AWS Consols Security Groups\n{AllSecurityGroups}")

if __name__== "__main__":
    DRYRUN = False

if args.group_id == securitygroups['GroupId']:
    print(f'The Security Group you are Inquiring About is Open to the Internet!!! \nHere is a description of the IP Range: {cidr}')
