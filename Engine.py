import pika
from ManualFunctions import check_if_perfect
from ManualFunctions import choose_function

import numbers
QUEUE_NAME_1 ='CLIENT'
QUEUE_NAME_2 = 'API'
def RMQ_on_request_CLIENT_message_received(ch, method, properties, body):
    #Handle RMQ requsets messages
    try:
        isinstance(int(body.decode("utf-8")), numbers.Integral)
        answer = check_if_perfect(int(body.decode("utf-8")))
        print(f"Sending the Answer to client:{answer}")
        ch.basic_publish('', routing_key=properties.reply_to, body=f'The Answer is : {answer}')
    except ValueError:
        print("Sending Input type incorect")
        ch.basic_publish('', routing_key=properties.reply_to, body=f'The Answer is : Sending Input type incorect')
        
def RMQ_on_request_API_message_received(ch, method, properties, body):
    print("API FUNC")   
    #sorte the options
    try:
        msg = choose_function(body.decode("utf-8"))
        ch.basic_publish('', routing_key=properties.reply_to, body=f'{msg}')
        
    except ValueError:
        print("somthing wrong") 
        ch.basic_publish('', routing_key=properties.reply_to, body=f'error')  
         
def start_RMQ_server():
    #This Function starts a RMQ Server
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME_1, durable=True)
    channel.queue_declare(queue=QUEUE_NAME_2, durable=True)
    
    
    channel.basic_consume(queue=QUEUE_NAME_1, auto_ack=True,
        on_message_callback=RMQ_on_request_CLIENT_message_received)
    
    channel.basic_consume(queue=QUEUE_NAME_2, auto_ack=True,
        on_message_callback=RMQ_on_request_API_message_received)
    print("Starting Server")
    channel.start_consuming()
    
def main():
    start_RMQ_server()

if __name__ == '__main__':
    main()

