import json
import os
import sys
import time
import pika

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_PORT = int(os.getenv("RABBITMQ_PORT", "5672"))
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "guest")
QUEUE_NAME = os.getenv("RABBITMQ_QUEUE", "aidd_tasks")


def callback(ch, method, properties, body):
    try:
        data = json.loads(body.decode("utf-8"))
        print(f"[Worker] Жаңа тапсырма алынды: {data}", flush=True)
        # Ұзақ уақыт алатын өңдеу (мысалы, LLM өңдеу немесе деректерді талдау)
        time.sleep(1)
        print(f"[Worker] Тапсырма сәтті аяқталды: {data.get('task_id', 'unknown')}", flush=True)
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as exc:
        print(f"[Worker] Қате: {exc}", file=sys.stderr, flush=True)
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)


def main():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        credentials=credentials,
        connection_attempts=10,
        retry_delay=5,
    )

    print(f"[Worker] RabbitMQ-ға қосылуда ({RABBITMQ_HOST}:{RABBITMQ_PORT})...", flush=True)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

    print(f"[Worker] Кезек дайын: '{QUEUE_NAME}'. Хабарламалар күтілуде...", flush=True)
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[Worker] Тоқтатылды.")
