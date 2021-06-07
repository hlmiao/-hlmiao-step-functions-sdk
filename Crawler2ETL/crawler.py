# Set up logging
import json
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Import Boto 3 for AWS Glue
import boto3
glue_client = boto3.client('glue')

# Variables for the job: 
crawlerName = "glue-demo-crawler-0222"

# Define Lambda function
def lambda_handler(event, context):
    print("Starting Glue Crawler")
    logger.info('## TRIGGERED BY EVENT: ')
    response = glue_client.start_crawler(Name = crawlerName)
    logger.info('## STARTED CRAWLER NAME: ' + crawlerName)
    return response
#   print("Glue Crawler is completed")
    logger.info('## END RequestId: ' + response['END RequestId'])