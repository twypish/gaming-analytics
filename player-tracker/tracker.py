from kafka import KafkaProducer
import json
import time
import random
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:29092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

games = ["Apex", "Valorant", "Halo", "League of Legends", "CS:GO", "Overwatch"]
event_types = ["kill", "death", "assist", "item_pickup", "objective", "healing", "gold_earned"]
match_ids = [f"match{i}" for i in range(1, 6)]

print("Event tracker started")

while True:
    game = random.choice(games)
    event = {
        "game_name": game,
        "match_id": random.choice(match_ids),
        "player_id": f"player{random.randint(1, 5)}",
        "event_type": random.choice(event_types),
        "value": random.randint(1, 5),
        "timestamp": datetime.utcnow().isoformat()
    }
    print("Sending event:", event)
    producer.send("player_events", event)
    time.sleep(1)
