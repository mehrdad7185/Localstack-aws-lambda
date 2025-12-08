
provider "aws" {
  region                      = "eu-central-1"
  access_key                  = "mehops"
  secret_key                  = "mehops"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    apigateway     = "http://localhost:4566"
    apigatewayv2   = "http://localhost:4566"
    cloudformation = "http://localhost:4566"
    cloudwatch     = "http://localhost:4566"
    dynamodb       = "http://localhost:4566"
    ec2            = "http://localhost:4566"
    es             = "http://localhost:4566"
    elasticache    = "http://localhost:4566"
    firehose       = "http://localhost:4566"
    iam            = "http://localhost:4566"
    kinesis        = "http://localhost:4566"
    lambda         = "http://localhost:4566"
    rds            = "http://localhost:4566"
    redshift       = "http://localhost:4566"
    route53        = "http://localhost:4566"
    s3             = "http://s3.localhost.localstack.cloud:4566"
    secretsmanager = "http://localhost:4566"
    ses            = "http://localhost:4566"
    sns            = "http://localhost:4566"
    sqs            = "http://localhost:4566"
    ssm            = "http://localhost:4566"
    stepfunctions  = "http://localhost:4566"
    sts            = "http://localhost:4566"
  }
}

resource "aws_dynamodb_table" "mehops_consumer_events" {
  name           = "mehops-consumer-events"
  read_capacity  = "20"
  write_capacity = "20"
  hash_key       = "Id"

  attribute {
    name = "Id"
    type = "S"
  }
}

resource "aws_sns_topic" "mehops_producer_topic" {
  name = "mehops-producer-events"
}

resource "aws_sqs_queue" "mehops_consumer_queue" {
  name = "mehops-consumer-events"
}

resource "aws_sns_topic_subscription" "mehops_sqs_subscription" {
  topic_arn = aws_sns_topic.mehops_producer_topic.arn
  protocol  = "sqs"
  endpoint  = aws_sqs_queue.mehops_consumer_queue.arn
  endpoint_auto_confirms = true
}