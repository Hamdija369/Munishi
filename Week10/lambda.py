import boto3

def CreateLambda(functionName):
    iam_client = boto3.client('iam')

    role_response = iam_client.get_role(RoleName='LabRole')
    lambda_client = boto3.client('lambda')

    handler = open('lambda_stop_function.zip', 'rb')
    zipped_code = handler.read()

    response = lambda_client.create_function(
        FunctionName = functionName,
        Role = role_response['Role']['Arn'],
        Publish = True,
        PackageType = 'Zip',
        Runtime = 'python3.9',
        Code={'ZipFile':zipped_code},
        Handler='lambda_stop_function.lambda_handler'
    )
    return response
##### - Added a new definition to add the Start function #####
def CreateLambda2(functionName):
    iam_client = boto3.client('iam')

    role_response = iam_client.get_role(RoleName='LabRole')
    lambda_client = boto3.client('lambda')

    handler = open('lambda_start_function.zip', 'rb')
    zipped_code = handler.read()

    response = lambda_client.create_function(
        FunctionName = functionName,
        Role = role_response['Role']['Arn'],
        Publish = True,
        PackageType = 'Zip',
        Runtime = 'python3.9',
        Code={'ZipFile':zipped_code},
        Handler='lambda_start_function.lambda_handler'
    )
    return response
#####

def InvokeLambda(functionName):
    lambda_client = boto3.client('lambda')
    response = lambda_client.invoke(FunctionName=functionName)
    return response

def main():
    functionName = 'StopEC2'
    lambda_client = boto3.client('lambda')
    try: 
        function = lambda_client.get_function(FunctionName=functionName)
    except lambda_client.exceptions.ResourceNotFoundException:
        print("Creating Function...")
        response = CreateLambda(functionName)
        print("Created Function")
    response = InvokeLambda(functionName)
    print(f"Status Code: {response['StatusCode']}")
    print(f"Status Code: {response}")
##### Added new for the start function 
def main2():
    functionName = 'StartEC2'
    lambda_client = boto3.client('lambda')
    try: 
        function = lambda_client.get_function(FunctionName=functionName)
    except lambda_client.exceptions.ResourceNotFoundException:
        print("Creating Function..2..")
        response = CreateLambda2(functionName)
        print("Created Function 2")    
    response = InvokeLambda(functionName)
    print(f"Status Code: {response['StatusCode']}")
    print(f"Status Code: {response}")
if __name__ == '__main__':
    main()
    main2()
