import pika
import uuid
msg = ''

def on_message(channel, method_frame, header_frame, body):
    global msg
    msg = body.decode("utf-8")
    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    channel.stop_consuming()
    
def send_to_rmqServer(var):
    #This function connect us with the Server
    if var == -1:
        #WE KNOW THAT IT OPTION 2
        #THEN WE SHOULD SEND X
        var = 'X'
    element = var
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    except pika.exceptions.AMQPConnectionError as exc:
        print("Failed to connect to RabbitMQ service. Message wont be sent.")
        return
    cor_id = str(uuid.uuid4())#generate a unique id
    channel = connection.channel()
    channel.queue_declare(queue='API', durable=True)
    reply_queue = channel.queue_declare(queue='', exclusive=True)

    channel.basic_publish(
        exchange='',
        routing_key='API',
        body=str(element),
        properties=pika.BasicProperties(
            reply_to=reply_queue.method.queue,
        correlation_id=cor_id
        )) 
    channel.basic_consume(queue=reply_queue.method.queue,on_message_callback=on_message)
    channel.start_consuming()
    channel.basic_cancel(reply_queue.method.queue)
    return msg

