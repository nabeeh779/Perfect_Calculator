import pika
import uuid

def get_input():
    #Gets the input from user
    return input("Enter a number to check:")
    
def on_reply_message_received(ch, method, properties, body):
    print(f"reply recieved: {body}")

def main():
    #Establish connection
    connection_parameters = pika.ConnectionParameters('localhost')
    connection = pika.BlockingConnection(connection_parameters)
    channel = connection.channel()

    reply_queue = channel.queue_declare(queue='', exclusive=True)

    channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True,
        on_message_callback=on_reply_message_received)
        
    channel.queue_declare(queue='request-queue')

    cor_id = str(uuid.uuid4())

    print("Starting Client")
    num = get_input()
    print(f"Sending Request: is {num} Perfect number?")
    channel.basic_publish('', routing_key='request-queue', properties=pika.BasicProperties(
        reply_to=reply_queue.method.queue,
        correlation_id=cor_id
    ), body=num)

    channel.start_consuming()




if __name__ == '__main__':
    main()
