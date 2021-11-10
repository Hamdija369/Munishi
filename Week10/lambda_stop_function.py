import json
import boto3
###
def Stop_EC2():
    ec2_client = boto3.client('ec2')
    instances = ec2_client.describe_instances(
#        Filters=[
#            {
#                'Name': 'tag:env',
#                'Values' : ['dev']
#            }
#        ]
    )
    instance_list = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_list.append(instance['InstanceId'])
    stop_response = ec2_client.stop_instances(InstanceIds=instance_list)
    return stop_response

def lambda_handler(event, context):
    #TODO implement
    stop_response = Stop_EC2()
    stopped_instances = []
    for instance in stop_response['StoppingInstances']:
        stopped_instances.append(instance['InstanceId'])

    return {
        'statusCode': 200,
        'body': json.dumps(stopped_instances)
    }
