# Project Architecture #
The project has a classic Web-Queue-Worker architecture. The core component of this architecture are a web
front-end that serves client requests, and a worker that performs tasks. The client communicates with the
worker through a message queue.   
More precisely -   

1. Client : a java/python AWS project (with one class that includes main method). It is hosted on your
machine (not on the cloud). This client does the following steps:   
• Creates an SQS Queue for requests (called the requestQueue) and use it to submit a request
containing a list of maximum 10 integers (separated by comments).   
• Receives the response from the EC2 worker.   

2. EC2 Worker: this is a java/python application that runs on an EC2 instance. It does the following
tasks:   
• Reads the messages from the requestQueue   
• Calculates the results   
• Creates a response queue (called responseQueue) and submits the result on it.   
• Create a new log file (a text file) and store it on Amazon S3.   

# Go Further: the hot-dog application #
You work for a very promising company which goal is to develop an app capable to recognize hot-dogs on
images. To proceed, the company needs labeled data, meaning data with a label 1 when it represents a
hot-dog ; 0 when it represents something else. You will create a new AWS application that shows a sample
of images to a client, let the client label each of the data, and store that label in a table.   
• The set of images available for labeling is stored in a S3 bucket   
• The file storing the label information for each image is also on a S3 bucket   
• Each client is shown 4 random images out of the total number of images that are in the bucket   
• If multiple client are shown the same image, you should record each answer in the same text file   
• A client can contribute and upload more hot-dog images to the bucket   
• You are free to choose whatever images you want to build you set of images (you need around 20 images). Half of these images must represent hot-dogs.   
• Choose small size image   

# Demonstration videos #   
https://youtube.com/playlist?list=PLeaWEbsy_j2_XKno6feYrWuUaO718RvlZ

# Our group #   
👤 Grégoire BIRON   
👤 Ruben FELICIANO   
👤 Thomas GAGNAIRE   

# Full subject #
https://mootse.telecom-st-etienne.fr/mod/resource/view.php?id=28548
