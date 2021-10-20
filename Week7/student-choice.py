import boto3
import json, datetime

# Adding the below so that when script is executed it is returned in a JSON format which will be easier to view/read. 
def defaultconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

cf_client = boto3.client('cloudformation') # Creating a function that will list out the Stack Name and Stack Status of any Stacks that we might have
response = cf_client.list_stacks()
#print(response['StackSummaries'])     #    To View a List of ALL stacks simply remove the # sign from Line# 13
for stacksummaries in response['StackSummaries']:
    formated_response = json.dumps(stacksummaries, default=defaultconverter,indent=4)    
#    print(f"My Stack Summaries are: {formated_response}")  # This command will print out the same as the command/scrip in line#11 However, it will return in JSON format for better viewing. 
    print(f"The Stack Name is: {stacksummaries['StackName']}") # This command Will only return the Stack Name of the Stack and nothing else. 
    print(f"The Status for this Stack is: {stacksummaries['StackStatus']}") # This command Will only return the status of the stack and nothing else. 

# For this portion of the assignment I had created a new stack named "Hamdi" from a script from the AWS Admin class. Was experimenting with it. Since I had only one Stack originally available. 
