import boto3
import datetime
import pytz
import json
##### #6 Midterm - List All Roles and Print Roles to the screen that were created in the last 90 days #####
client = boto3.client('iam')
roles = client.list_roles()
Role_list = roles['Roles']
for key in Role_list:
     if key['CreateDate'] > (pytz.utc.localize(datetime.datetime.utcnow())-datetime.timedelta(days=90)):
        print(f'Role Name: - {key["RoleName"]}')
        print(f'Creation Date: - {key["CreateDate"]}')
##### #7 Midetem - List a role's policies and list just the POLICY NAME for the roles that are newer than 90 days #####
response = client.list_policies(
    Scope='All',
    OnlyAttached=True
) 
paginator = client.get_paginator("list_policies")
for page in paginator.paginate():
    for policy in page['Policies']:
        if policy['CreateDate'] > (pytz.utc.localize(datetime.datetime.utcnow())-datetime.timedelta(days=90)):
            print(f'Policy Name: - {policy["PolicyName"]}')
            print(f'Creation Date: - {policy["CreateDate"]}')
##########Hamdi 10/20/2021##########
