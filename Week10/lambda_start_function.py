import json
import boto3

def Start_EC2():
    ec2_client = boto3.client('ec2')
    instances = ec2_client.describe_instances()
    instance_list = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_list.append(instance['InstanceId'])
    start_response = ec2_client.start_instances(InstanceIds=instance_list)
    return start_response

def lambda_handler(event, context):
    #TODO implement
    start_response = Start_EC2()
    started_instances = []
    for instance in start_response['StartingInstances']:
        started_instances.append(instance['InstanceId'])

    return {
        'statusCode': 200,
        'body': json.dumps(started_instances)
    }
