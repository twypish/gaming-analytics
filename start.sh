#!/bin/bash

echo "Stopping and removing any previously running containers..."

docker rm -f kafka zookeeper redis 2>/dev/null

echo "Starting Zookeeper..."
docker run -d --name zookeeper \
  -p 2181:2181 \
  -e ZOOKEEPER_CLIENT_PORT=2181 \
  -e ZOOKEEPER_TICK_TIME=2000 \
  confluentinc/cp-zookeeper:7.2.1

echo "Starting Kafka..."
docker run -d --name kafka \
  --link zookeeper \
  -p 29092:29092 \
  -e KAFKA_BROKER_ID=1 \
  -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:29092 \
  -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=PLAINTEXT:PLAINTEXT \
  -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 \
  confluentinc/cp-kafka:7.2.1

echo "Starting Redis..."
docker run -d --name redis -p 6379:6379 redis

echo "Waiting for Kafka to become available..."
until docker exec kafka /usr/bin/kafka-topics --bootstrap-server localhost:29092 --list &>/dev/null; do
  sleep 2
done

echo "Creating Kafka topic 'player_events' if it doesn't exist..."
docker exec kafka /usr/bin/kafka-topics \
  --bootstrap-server localhost:29092 \
  --create --if-not-exists \
  --topic player_events \
  --partitions 1 \
  --replication-factor 1

if lsof -i :5000 &>/dev/null; then
  echo "Port 5000 is in use. Killing previous Flask app..."
  fuser -k 5000/tcp
fi

echo "Starting Flask API..."
python3 leaderboard-service/app.py &

echo "Starting Kafka Consumer..."
python3 analytics-engine/consumer.py &

echo "Starting Kafka Tracker (Producer)..."
python3 player-tracker/tracker.py &

tail -f /dev/null

