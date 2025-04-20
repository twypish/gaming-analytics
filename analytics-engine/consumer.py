from kafka import KafkaConsumer
import json
import redis

# Connect to Kafka
consumer = KafkaConsumer(
    "player_events",
    bootstrap_servers='localhost:29092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='analytics-group'
)

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

print("Analytics Engine running...")

for message in consumer:
    event = message.value
    player_id = event["player_id"]
    event_type = event["event_type"]

    # Redis hash key
    redis_key = f"stats:{player_id}"

    if event_type == "kill":
        r.hincrby(redis_key, "kills", 1)
    elif event_type == "death":
        r.hincrby(redis_key, "deaths", 1)
    elif event_type == "item_pickup":
        r.hincrby(redis_key, "items", 1)

    # Optional: Print updated stats
    stats = r.hgetall(redis_key)
    decoded_stats = {k.decode(): int(v) for k, v in stats.items()}
    print(f"{player_id} stats: {decoded_stats}")

