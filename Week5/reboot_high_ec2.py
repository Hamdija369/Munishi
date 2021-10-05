import ec2
import boto3
import sns

DRYRUN = False

sts_client = boto3.client('sts')
response = sts_client.get_caller_identity()
account_id = response['Account']
#print(f"Account ID is {account_id}")

ec2_client = boto3.client('ec2')

image_id = ec2.Get_Image(ec2_client)
#print(f"Image ID is {image_id}")

instance_id = ec2.Create_EC2(image_id,ec2_client)
print(f"Instance ID: {instance_id}")

cw_client = boto3.client('cloudwatch')

sns_topic = sns.CreateSNSTopic("High-CPU-notification")
response = sns.SubscribeEmail(sns_topic,"munishi@madisoncollege.edu")

response = cw_client.put_metric_alarm(
    AlarmName='Web_Server_HIGH_CPU_Utilization',
    ComparisonOperator='GreaterThanOrEqualToThreshold',
    EvaluationPeriods=2,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Period=100,
    Statistic='Average',
    Threshold=71.0,
    ActionsEnabled=True,
    AlarmActions=[
        f'arn:aws:swf:us-east-1:{account_id}:action/actions/AWS_EC2.InstanceId.Reboot/1.0',
        f'arn:aws:sns:us-east-1:{account_id}:High-CPU-notification'
    ],
    AlarmDescription='Alarm when server CPU is greater than 70%',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': instance_id
        },
    ]
)