
import boto3
import time
sqs = boto3.resource('sqs')
# Get the queue
sqs.create_queue(QueueName='test')
sqs.create_queue(QueueName='reponse')
