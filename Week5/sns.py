import boto3

def CreateSNSTopic(topic_name):
    sns_client = boto3.client('sns')
    response = sns_client.create_topic(Name=topic_name)
    return response["TopicArn"]

def SubscribeEmail(topic_arn,email):
    sns_client = boto3.client('sns')
    response = sns_client.subscribe(TopicArn=topic_arn,Endpoint=email,Protocol='email')
    return response["SubscriptionArn"]
