import boto3
from botocore.exceptions import ClientError

ec2_client = boto3.client('ec2')
############################################################################################################################
#Listing all EC2 instances and the Security Groups of each Instance.                                                       #
####################################################################                                                       #
try:                                                                                                                       #
    response = ec2_client.describe_instances()                                                                             #
    for reservation in response['Reservations']:                                                                           #
        for instance in reservation['Instances']:                                                                          #
            print("Instance: " + instance['InstanceId'])                                                                   #
            for securityGroup in instance['SecurityGroups']:                                                               #
                print("--Security Group ID: {}, Name: {}".format(securityGroup['GroupId'], securityGroup['GroupName']))    #
except Exception as E:                                                                                                     #
    print(E)                                                                                                               #
############################################################################################################               #
# This above script returns an Instance ID and any Security Groups ID & Name associated with those Instances               #
############################################################################################################################

###################################################################
#Checking each Security Group to ensure that port 22 is not open. #
##############################################################    #
ec2_r = boto3.resource('ec2')                                     #
security_groups = ec2_r.security_groups.filter(                   #
    Filters=[                                                     #
        {                                                         #
            "Name": "ip-permission.from-port",                    #
            "Values": ["22"]                                      #
        }                                                         #
    ]                                                             #
)                                                                 #
print('\nList of Security Groups - That Have Port 22 OPEN:')      #
for security_group in security_groups:                            #
    print(f' - Security Group {security_group.id} ')              #
##############################################################    #
# This above script looks through all of the security groups      #
# and returns only the ID's of the security groups with port 22.  #
# If no security groups with port 22 - no reponse is returned     #
###################################################################

##################################################################################################################################
#If Port 22 is open we are using the revoke_security_group_ingress() function to remove access to port 22.                       #
###########################################################################################################                      #
ec2_client = boto3.client('ec2')                                                                                                 #
response = ec2_client.describe_security_groups(                                                                                  #
    Filters=[                                                                                                                    #
        {                                                                                                                        #
            "Name": "ip-permission.from-port",                                                                                   #
            "Values": ["22"]                                                                                                     #
        }])                                                                                                                      #
for group in response['SecurityGroups']:                                                                                         #
    ec2_client.revoke_security_group_ingress(GroupId=group['GroupId'], IpPermissions = group['IpPermissions'])                   #
    print(f"\nSuccessfully Revoked Access to Port 22 for Security Group: {group['GroupId']}, Name: {group['GroupName']}")        #                      #
####################################################################################################################             #
# This above script takes ALL security groups that have port 22 open and revokes that rule for those security groups.            #
# A bit redundant but I felt more comfortable with using client instead of resource so you see what seems like a duplicate       #
# filter.   Once a rule for port 22 is revoked you will get a message indicating that, as well as letting you know the           #
# exact Security Group that the port 22 was revoked from.                                                                        #                                                                                           #
##################################################################################################################################
