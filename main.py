# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import boto3;


# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')
#queue.purge()
print('entrez plusieurs entier : ')
a = [int(x) for x in input().split()]
print(a);


response = queue.send_message(MessageBody='boto3', MessageAttributes={
        'entier1': {
            'DataType': 'Number',
            'StringValue': str(a[0])

        },
        'entier2': {
            'DataType': 'Number',
            'StringValue': str(a[1])
        },
        'entier3': {
            'DataType': 'Number',
            'StringValue': '0'
        },
        'entier4': {
            'DataType': 'Number',
            'StringValue': '0'
        },
        'entier5': {
            'DataType': 'Number',
            'StringValue': '0'
        },
        'entier6': {
            'DataType': 'Number',
            'StringValue': '0'
        },
        'entier7': {
            'DataType': 'Number',
            'StringValue': '0'
        },
        'entier8': {
            'DataType': 'Number',
            'StringValue': '0'
        },
        'entier9': {
            'DataType': 'Number',
            'StringValue': '0'
        }
    },)




# Process messages by printing out body and optional author name
for message in queue.receive_messages(MessageAttributeNames=['entier1']):
    # Get the custom author message attribute if it was set
    author_text = ''
    if message.message_attributes is not None:
        author_name = message.message_attributes.get('entier1').get('StringValue')

        if author_name:
            author_text = ' ({0})'.format(author_name)

    # Print out the body and author (if set)
    print('Hello, '+ author_name )

    # Let the queue know that the message is processed
    message.delete()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
