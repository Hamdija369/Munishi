terraform {
    backend "remote"{
        organization = "Scripting4Cloud"
        workspaces {
            name = "Hamdi-Demo-Workspace"
        }
    }
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 3.27"
        }
    }

    required_version = ">= 0.14.9"
}

provider "aws" {
    profile = "default"
    region = "us-east-1"
}

data "aws_iam_role" "lab_role" {
    name = "LabRole"
}

resource "aws_lambda_function" "test_lambda"{
    filename = "StopEC2.zip"
    function_name = "hamdi-StopEC2"
    role = data.aws_iam_role.lab_role.arn
    runtime = "python3.9"
    handler = "StopEC2.lambda_handler"
}

data "aws_iam_role" "lab_role2" {
    name = "LabRole"
}

resource "aws_lambda_function" "test2_lambda"{
    filename = "StartEC2.zip"
    function_name = "hamdi-StartEC2"
    role = data.aws_iam_role.lab_role2.arn
    runtime = "python3.9"
    handler = "StartEC2.lambda_handler"
}
