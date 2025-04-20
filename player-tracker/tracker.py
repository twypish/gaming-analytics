from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:29092',  # External Kafka port
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Convert dict to JSON
)

# Simulated event types
event_types = ["kill", "death", "item_pickup"]

# Loop to send events continuously
while True:
    event = {
        "player_id": f"player{random.randint(1, 5)}",
        "event_type": random.choice(event_types),
        "timestamp": datetime.utcnow().isoformat(),
        "match_id": "match1"
    }

    print("Sending event:", event)
    producer.send("player_events", event)
    time.sleep(1)  # Send one event per second

