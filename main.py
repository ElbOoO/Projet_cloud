# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import boto3
import time

# Get the service resource
sqs = boto3.resource('sqs')
# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')
print('entrez plusieurs entier : ')
a = [int(x) for x in input().split()]
print(a)
print(len(a))
#queue.purge()
queue = sqs.get_queue_by_name(QueueName='test')

if len(a)>0:
    entier1 = str(a[0])
else :
    entier1 =0
if len(a)>1:
    entier2 = str(a[1])
else:
    entier2 = 0
if len(a)>2:
    entier3 = str(a[2])
else:
    entier3 = 0
if len(a)>3:
    entier4 = str(a[3])
else :
    entier4 =0
if len(a)>4:
    entier5 = str(a[4])
else :
    entier5 =0
if len(a)>5:
    entier6 = str(a[5])
else :
    entier6 =0
if len(a)>6:
    entier7 = str(a[6])
else :
    entier7 =0
if len(a)>7:
    entier8 = str(a[7])
else :
    entier8 =0
if len(a)>8:
    entier9 = str(a[8])
else :
    entier9 =0
if len(a)>9:
    entier10 = str(a[9])
else :
    entier10 =0




response = queue.send_message(MessageBody='boto3', MessageAttributes={
        'entier1': {
            'DataType': 'Number',
            'StringValue': str(entier1)

        },
        'entier2': {
            'DataType': 'Number',
            'StringValue': str(entier2)
        },
        'entier3': {
            'DataType': 'Number',
            'StringValue': str(entier3)
        },
        'entier4': {
            'DataType': 'Number',
            'StringValue': str(entier4)
        },
        'entier5': {
            'DataType': 'Number',
            'StringValue': str(entier5)
        },
        'entier6': {
            'DataType': 'Number',
            'StringValue': str(entier6)
        },
        'entier7': {
            'DataType': 'Number',
            'StringValue': str(entier7)
        },
        'entier8': {
            'DataType': 'Number',
            'StringValue': str(entier8)
        },
        'entier9': {
            'DataType': 'Number',
            'StringValue': str(entier9)
        }
    },)

#-----------------------------------------------    serveur side    ---------------------------------------------------
#---------------------------------------------   client side  ----------------------------------------------------------
queue2 = sqs.get_queue_by_name(QueueName='reponse')


toto2 = True
while (toto2):
    time.sleep(1)
    print("waiting for message to come")
    for message in queue2.receive_messages(MessageAttributeNames=['All']):
        # Get the custom author message attribute if it was set
        author_text = ''
        if message.message_attributes is not None:
            reponse = message.message_attributes.get('entier1').get('StringValue')
            toto2 = False
            message.delete()

        # Print out the body and author (if set)
        print('vois tu la réponse , ' + reponse)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/


