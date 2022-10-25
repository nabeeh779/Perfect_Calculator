import pika
from ManualFunctions import check_if_perfect


def on_request_message_received(ch, method, properties, body):
    answer = check_if_perfect(int(body.decode("utf-8")))
    print(f"Sending the Answer to client:{answer}")
    ch.basic_publish('', routing_key=properties.reply_to, body=f'The Answer is : {answer}')


def main():
    connection_parameters = pika.ConnectionParameters('localhost')

    connection = pika.BlockingConnection(connection_parameters)

    channel = connection.channel()

    channel.queue_declare(queue='request-queue')

    channel.basic_consume(queue='request-queue', auto_ack=True,
        on_message_callback=on_request_message_received)

    print("Starting Server")

    channel.start_consuming()

if __name__ == '__main__':
    main()

