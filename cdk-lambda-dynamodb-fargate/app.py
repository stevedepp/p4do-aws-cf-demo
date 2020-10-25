#!/usr/bin/env python3

from aws_cdk import core

from cdk_lambda_dynamodb_fargate.cdk_lambda_dynamodb_stack import CdkLambdaDynamodbStack

app_env = {"region": "us-east-1"}
app = core.App()
CdkLambdaDynamodbStack(app, "cdk-lambda-dynamodb", env=app_env)

app.synth()
