import boto3
###
def Stop_EC2():
    ec2_client = boto3.client('ec2')
    instances = ec2_client.describe_instances(
        Filters=[
            {
                'Name': 'tag:env',
                'Values' : ['dev']
            }
        ]
    )
    instance_list = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_list.append(instance['InstanceId'])
    stop_response = ec2_client.stop_instances(InstanceIds=instance_list)
    return stop_response

def Start_EC2():
    ec2_client = boto3.client('ec2')
    instances = ec2_client.describe_instances()
    instance_list = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_list.append(instance['InstanceId'])
    start_response = ec2_client.start_instances(InstanceIds=instance_list)
    return start_response

def main():
    stop_response = Stop_EC2()
    print(f"Stop Response = {stop_response}")
    start_response = Start_EC2()
    print(f"Start Response = {start_response}")

if __name__ == '__main__':
    main()