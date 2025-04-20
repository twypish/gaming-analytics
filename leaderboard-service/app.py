from flask import Flask, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    players = []
    keys = r.keys('stats:*')

    for key in keys:
        player_id = key.decode().split(':')[1]
        stats = r.hgetall(key)
        decoded_stats = {k.decode(): int(v) for k, v in stats.items()}
        score = decoded_stats.get("kills", 0) - decoded_stats.get("deaths", 0)
        players.append({
            "player_id": player_id,
            "kills": decoded_stats.get("kills", 0),
            "deaths": decoded_stats.get("deaths", 0),
            "items": decoded_stats.get("items", 0),
            "score": score
        })

    # Sort by score descending
    sorted_players = sorted(players, key=lambda x: x["score"], reverse=True)
    return jsonify(sorted_players)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

