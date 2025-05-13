from flask import Flask, jsonify, request
from flask_cors import CORS
import redis

app = Flask(__name__)
CORS(app)

r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    game = request.args.get('game')
    if not game:
        return jsonify({"error": "Missing 'game' query parameter"}), 400

    keys = r.keys(f'stats:{game}:*')
    players = []
    for key in keys:
        player_id = key.decode().split(':')[2]
        stats = r.hgetall(key)
        decoded_stats = {k.decode(): int(v) for k, v in stats.items()}
        score = (
            2 * decoded_stats.get("kill", 0)
            + decoded_stats.get("assist", 0)
            + decoded_stats.get("item_pickup", 0)
            + 3 * decoded_stats.get("objective", 0)
            + decoded_stats.get("gold_earned", 0)
            + decoded_stats.get("healing", 0)
            - decoded_stats.get("death", 0)
        )
        players.append({
            "player_id": player_id,
            "score": score,
            **decoded_stats
        })

    sorted_players = sorted(players, key=lambda x: x["score"], reverse=True)
    return jsonify(sorted_players)

@app.route('/games', methods=['GET'])
def list_games():
    keys = r.keys('stats:*')
    games = {key.decode().split(':')[1] for key in keys if len(key.decode().split(':')) == 3}
    return jsonify(sorted(games))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
