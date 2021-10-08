# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import boto3;


# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('entrez plusieurs entier : ')

response = queue.send_message(MessageBody='boto3', MessageAttributes={
        'entier1': {
            'DataType': 'Number',
            'StringValue': '5'
        },
        'entier2': {
            'DataType': 'Number',
            'StringValue': '3'
        },
        'entier3': {
            'DataType': 'Number',
            'StringValue': '6'
        }
    },)




# Process messages by printing out body and optional author name
for message in queue.receive_messages(MessageAttributeNames=['Author']):
    # Get the custom author message attribute if it was set
    author_text = ''
    if message.message_attributes is not None:
        author_name = message.message_attributes.get('Author').get('StringValue')

        if author_name:
            author_text = ' ({0})'.format(author_name)

    # Print out the body and author (if set)
    print('Hello, '+ author_name )

    # Let the queue know that the message is processed
    message.delete()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
