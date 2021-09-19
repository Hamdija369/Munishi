import boto3
DRYRUN = False

ec2_client = boto3.client('ec2')
ec2_instance = boto3.resource('ec2')

def Get_Image(ec2_client):
    
    images = ec2_client.describe_images(
        Filters=[
            {
                'Name': 'name',
                'Values' : ['amzn2-ami-hvm*']
            }
        ]
    )
    return images["Images"][0]['ImageId']

def Create_EC2(AMI,ec2_client):
    
    response = ec2_client.run_instances(

        ImageId=AMI,
        InstanceType='t2.micro',
        MaxCount=1,
        MinCount=1,
        DryRun = DRYRUN
    )
    return response['Instances'][0]['InstanceId']

def Print_Tags(ec2):
    tags=ec2.tags
    if ec2.tags : 
        for tag in ec2.tags:
            print(tag)      
    else:
        print('No Tags Found Here')

def Create_Tag(ec2,key,value):
    ec2.create_tags(
        DryRun=DRYRUN,
        Tags=[
        {
            'Key': key,
            'Value': value,
        },
    ]
)

if __name__== "__main__":
    DRYRUN = False

    ec2_client = boto3.client('ec2')
    ec2_instance = boto3.resource('ec2')
    AMI = Get_Image(ec2_client)
    instance_id = Create_EC2(AMI, ec2_client)
    ec2 = ec2_instance.Instance(instance_id)
    ec2.wait_until_running()
    print(f"Instanace created, state is: {ec2.state['Name']}")
    print(f"Instanace created, Public IP Address is: {ec2.public_ip_address}") 
    Print_Tags(ec2)
    Create_Tag(ec2, "Name","Hamdi")
    Print_Tags(ec2)
    ec2.terminate()
    ec2.wait_until_terminated()
    print(f"Instanace terminated, state is: {ec2.state['Name']}")
