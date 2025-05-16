# Real-Time Gaming Analytics Generator

The Real-Time Gaming Analytics Generator is a full-stack microservices project designed to simulate and analyze live event data from competitive multiplayer games. Built as a solo project, this system captures in-game events, processes them through a Kafka pipeline, and updates real-time leaderboards via a responsive web interface.

Designed and developed by Troy Wypishinski-Prechter as part of a graduate-level machine learning and systems engineering initiative.

---

## Features

- Real-time stat tracking: kills, assists, deaths, and score
- Dynamic leaderboards for multiple games (Apex Legends, Valorant, Halo)
- Kafka-based streaming pipeline for scalable ingestion
- Redis-backed analytics engine with low-latency computation
- RESTful Flask API for frontend data access
- React-based live dashboard with automatic updates
- Dockerized architecture for local or cloud deployment

---

## Architecture Overview

```

Event Producer(s) ---> Kafka ---> Analytics Engine ---> Redis ---> Flask API ---> React Frontend

```

Each component is independently containerized and designed for horizontal scaling.

---

## Project Structure

```

gaming-analytics/
├── api/                 # Flask API for leaderboard data
├── analytics/           # Kafka consumer and Redis updater
├── event-producer/      # Simulated game event generator
├── frontend/            # React-based dashboard interface
├── docker-compose.yml   # Docker orchestration
└── README.md

````

---

## Tech Stack

| Layer         | Technology            |
|--------------|------------------------|
| Event Stream | Apache Kafka           |
| Processing   | Python, Redis          |
| Backend API  | Flask                  |
| Frontend     | React, Axios           |
| Deployment   | Docker, Docker Compose |
| Storage      | PostgreSQL (planned)   |

---

## How to Run Locally

1. Clone the repository:
   ```bash
   git clone git@github.com:twypish/gaming-analytics.git
   cd gaming-analytics
````

2. Start all services with Docker Compose:

   ```bash
   docker-compose up --build
   ```

3. Open the dashboard in your browser:

   ```
   http://localhost:3000
   ```

4. Start simulating game events:

   ```bash
   docker exec -it event-producer python simulate.py
   ```

---

## Use Cases

* Real-time dashboards for esports tournaments
* Analytics backend for indie or multiplayer game developers
* Leaderboard integration into web or game clients
* Internal data pipelines for game event analysis

---

## Planned Improvements

If extended, the system would include:

* User authentication and stat history persistence
* Kubernetes-based deployment for autoscaling
* Integration with actual game APIs (e.g., Riot, Steam)
* Predictive scoring models and visualization (heatmaps, trends)
* Admin panel for scoring configuration and monitoring

---

## Lessons Learned

* Designed an end-to-end microservices pipeline from scratch
* Developed proficiency with Kafka message processing
* Built and synced API and frontend for real-time responsiveness
* Leveraged Docker Compose to orchestrate multi-container environments
* Gained experience in modular design and system extensibility

---

## Contact

Troy Wypishinski-Prechter
Email: twypish@gmail.com
Website: https://twypish.dev
LinkedIn: https://linkedin.com/in/tjwp
GitHub: https://github.com/twypish

---

## License

This project is open source and available under the MIT License.
