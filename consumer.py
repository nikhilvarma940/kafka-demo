from kafka import KafkaConsumer
import json

TOPIC = 'test'
BOOTSTRAP_SERVERS = ['172.51.1.11:9092']

if __name__ == "__main__":
    consumer = KafkaConsumer(
        TOPIC,                                  # topic
        bootstrap_servers=BOOTSTRAP_SERVERS,    # kafka server
        auto_offset_reset='earliest',           # 'earliest' consume from beginning;
                                                # else 'latest' (default) from last offset consumed
        group_id="consumer-group-a")            # group id

    print("starting the consumer")
    for msg in consumer:
        print("Registered User = {}".format(
            json.loads(msg.value)))             # parse serialised values


        pip install kakfa-python 
        pip install Faker