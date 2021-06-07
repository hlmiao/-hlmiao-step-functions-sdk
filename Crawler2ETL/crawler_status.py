import json
#from botocore.exceptions import ClientError
import boto3

glue_client = boto3.client('glue')

def lambda_handler(event, context):
    
    class CrawlerInProgressException(Exception):
        pass
    
    # Extract Parametres from Event (invoked by StepFunctions)
    
    crawler_name = 'glue-demo-crawler-0222'
    
    response = glue_client.get_crawler_metrics(CrawlerNameList =[crawler_name])
    print(response['CrawlerMetricsList'][0]['CrawlerName']) 
    print(response['CrawlerMetricsList'][0]['TimeLeftSeconds']) 
    print(response['CrawlerMetricsList'][0]['StillEstimating']) 
    
    if (response['CrawlerMetricsList'][0]['StillEstimating']):
        raise CrawlerInProgressException('Crawler In Progress!')
    elif (response['CrawlerMetricsList'][0]['TimeLeftSeconds'] > 0):
        raise CrawlerInProgressException('Crawler In Progress!')