localstack Desktop for Mac , Linux and Windows
https://docs.localstack.cloud/aws/capabilities/web-app/localstack-desktop/
LocalStack AWS Lambda Practice

This repository contains a set of small experiments to practice
AWS-style serverless workflows locally using LocalStack. The goal is to
understand how services like Lambda, S3, DynamoDB, SNS, and SQS interact
in an event-driven architecture without using the real AWS cloud.

Repository: https://github.com/mehrdad7185/Localstack-aws-lambda

What this project demonstrates - Running AWS services locally with
LocalStack - Creating Lambda functions using Python and boto3 -
Connecting Lambda to DynamoDB - Triggering Lambda when files are
uploaded to S3 - Basic message flow using SNS and SQS - Practicing
infrastructure setup with AWS CLI

Requirements - Docker - LocalStack - AWS CLI - Python 3 - boto3

Useful links LocalStack: https://github.com/localstack/localstack

LocalStack Desktop: https://www.localstack.cloud

AWS CLI: https://docs.aws.amazon.com/cli/

boto3: https://github.com/boto/boto3

How the examples generally work

Example flow (S3 -> Lambda): 1. A file is uploaded to an S3 bucket. 
2.S3 generates an event. 
3. The event triggers a Lambda function. 
4.Lambda reads information about the uploaded file. 
5. The function prints logs or processes the data.

This is similar to real-world systems where uploads trigger background
processing.

Running LocalStack

Install and start LocalStack:
```
localstack start
```
Configure AWS CLI for LocalStack:
```
export AWS_ACCESS_KEY_ID=test 
export AWS_SECRET_ACCESS_KEY=test 
export AWS_DEFAULT_REGION=us-east-1
```
Test connection:
```
aws dynamodb list-tables –endpoint-url=http://localhost:4566
```
Project structure (simplified)

simple_s3/ src/ handler.py simple_s3_payload.zip

auth_lambda/ image_processor/

Each folder contains a Lambda example and the zip package used to deploy
it.

Purpose of the repository

This repo is mainly for learning and experimentation. It helps
understand: - Event-driven architecture - Lambda triggers - How AWS
services communicate - Local cloud simulation for development

Author Mehrdad
