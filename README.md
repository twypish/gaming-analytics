# Real-Time Gaming Analytics Platform

A microservices-based system for tracking and displaying real-time multiplayer game analytics. Designed using Kafka, Redis, Flask, and React.

## Overview

This project simulates real-time gameplay events and processes them through a scalable microservices architecture. It tracks player activity (kills, deaths, item pickups) and displays a constantly updating leaderboard through a live React dashboard.

## Architecture

- Kafka — Handles real-time message streaming of player events  
- Zookeeper — Supports Kafka coordination  
- Redis — Stores real-time player statistics  
- Flask (Leaderboard API) — Aggregates Redis data and exposes `/leaderboard` endpoint  
- React — Frontend UI that polls and displays the live leaderboard  
- Docker Compose — Orchestrates all services for easy deployment

## Features

- Real-time simulated player event tracking  
- Live leaderboard display with automatic updates  
- Scalable microservices design  
- Easily extensible to include more analytics (damage dealt, healing, etc.)

## Project Structure

```
gaming-analytics/
├── analytics-engine/       # Kafka consumer, writes stats to Redis
├── player-tracker/         # Kafka producer, simulates gameplay
├── leaderboard-service/    # Flask app that reads Redis and serves leaderboard API
├── leaderboard-frontend/   # React app for displaying leaderboard
├── docker-compose.yml      # Brings everything together
```

## Getting Started

### Prerequisites

- Python 3  
- pip  
- Docker & Docker Compose  
- Node.js & npm (for React frontend)

### Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/gaming-analytics.git
cd gaming-analytics
```

2. Install Python dependencies:

```
pip install flask flask-cors redis kafka-python
```

3. Start Kafka, Redis, Zookeeper, and Kafka UI:

```
docker-compose up -d
```

4. Start Flask leaderboard API:

```
cd leaderboard-service
python app.py
```

5. Start React frontend:

```
cd leaderboard-frontend
npm install
npm start
```

6. Start Player Tracker and Analytics Engine in separate terminals:

```
cd player-tracker && python tracker.py
cd analytics-engine && python consumer.py
```

## Demo

- React Dashboard: http://localhost:3000  
- Leaderboard API: http://localhost:5000/leaderboard  
- Kafka UI: http://localhost:8080

## Date

Last updated: April 19, 2025

## Author

Troy Wypishinski-Prechter — twypish.dev — GitHub: https://github.com/twypish
```
