from ast import If
import pika
import uuid
import Save
from ManualFunctions import get_input
import os,sys
QUEUE_NAME_1 ='CLIENT'
def on_reply_message_received(ch, method, properties, body):
        
    print(f"reply recieved: {body}")
    
def start_RMQ_client(queueName,var):
    global TEMP
    TEMP = queueName
    #Establish connection
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    
    reply_queue = channel.queue_declare(queue='', exclusive=True)
    channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True,on_message_callback=on_reply_message_received)   
    #channel.queue_declare(queue=QUEUE_NAME_1)
    
    cor_id = str(uuid.uuid4())#generate a unique id
    
    print("Starting Client")
    num = get_input()
    print(f"Sending Request: is {num} Perfect number?")
    
    channel.basic_publish('', routing_key=queueName, properties=pika.BasicProperties(
        reply_to=reply_queue.method.queue,
        correlation_id=cor_id
    ), body=num)

    channel.start_consuming()
    
def main():
    start_RMQ_client(QUEUE_NAME_1,0)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)