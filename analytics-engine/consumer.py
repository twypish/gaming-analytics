from kafka import KafkaConsumer
import json
import redis

consumer = KafkaConsumer(
    "player_events",
    bootstrap_servers='localhost:29092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='analytics-group'
)

r = redis.Redis(host='localhost', port=6379, db=0)
print("Analytics engine started")

for message in consumer:
    event = message.value
    player_id = event.get("player_id")
    game_name = event.get("game_name", "default_game")
    event_type = event.get("event_type")
    value = event.get("value", 1)

    redis_key = f"stats:{game_name}:{player_id}"
    r.hincrby(redis_key, event_type, value)
