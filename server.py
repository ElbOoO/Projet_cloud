import datetime

import boto3
import time
import os
from time import strftime

sqs = boto3.resource('sqs')
# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')

bucket_name ='cloudcomputing-i-pro'

client_s3 =boto3.client(
    's3'
)
aujour = datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')


toto = True
while (toto):
    time.sleep(1)
    print("waiting for message to come")
    for message in queue.receive_messages(MessageAttributeNames=['All']):
        # Get the custom author message attribute if it was set
        author_text = ''
        if message.message_attributes is not None:
            entier1 = message.message_attributes.get('entier1').get('StringValue')
            entier2 = message.message_attributes.get('entier2').get('StringValue')
            entier3 = message.message_attributes.get('entier3').get('StringValue')
            entier4 = message.message_attributes.get('entier4').get('StringValue')
            entier5 = message.message_attributes.get('entier5').get('StringValue')
            entier6 = message.message_attributes.get('entier6').get('StringValue')
            entier7 = message.message_attributes.get('entier6').get('StringValue')
            entier8 = message.message_attributes.get('entier6').get('StringValue')
            entier9 = message.message_attributes.get('entier6').get('StringValue')
            toto = False
            message.delete()

        # Print out the body and author (if set)
        print('Le message est bien arrivé, on calcul la somme :')
file = open(os.getcwd() +aujour +"log.txt", "w")
file.write("\n"+(datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S'))+': reception des données ')



sum = int(entier1) + int(entier2) + int(entier3) + int(entier4) + int(entier5) + int(entier6)+ int(entier7) + int(entier8) + int(entier9)
print('la somme est égale à : ' +str(sum))
file.write("\n"+(datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S')))
file.write(': somme calculée = '+ str(sum) )

queue2 = sqs.get_queue_by_name(QueueName='reponse')
response = queue2.send_message(MessageBody='boto3', MessageAttributes={
        'entier1': {
            'DataType': 'Number',
            'StringValue': str(sum)
        }
    },)
print('Reponse bien envoyé ')

file.write("\n"+str(datetime.datetime.today().strftime('%Y-%m-%d-%H-%M-%S'))+": Envoi du fichier")

file.close()
client_s3.upload_file(
        os.getcwd()+aujour+"log.txt",
        bucket_name,
        "log/"+aujour+'log.txt'
)
