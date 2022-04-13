from kafka import KafkaProducer
import json
from data import get_registered_user
import time

TOPIC = 'test'
BOOTSTRAP_SERVERS = ['172.51.1.11:9092']

def json_serializer(data):
    return json.dumps(data).encode("utf-8")


producer = KafkaProducer(BOOTSTRAP_SERVERS,
                         value_serializer=json_serializer,
                         )

if __name__ == "__main__":
    i = 1
    while 1 == 1:
        registered_user = get_registered_user()
        print(i, registered_user)
        i += 1
        producer.send("registered_user", TOPIC)
        time.sleep(5)
        
