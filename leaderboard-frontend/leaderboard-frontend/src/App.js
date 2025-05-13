import React, { useEffect, useState } from 'react';

function App() {
  const [games, setGames] = useState([]);
  const [selectedGame, setSelectedGame] = useState('');
  const [players, setPlayers] = useState([]);

  useEffect(() => {
    // Fetch list of available games
    const fetchGames = async () => {
      try {
        const response = await fetch('http://localhost:5000/games');
        const data = await response.json();
        setGames(data);
        if (data.length > 0) setSelectedGame(data[0]);
      } catch (err) {
        console.error('Failed to fetch games:', err);
      }
    };
    fetchGames();
  }, []);

  useEffect(() => {
    if (!selectedGame) return;

    const fetchLeaderboard = async () => {
      try {
        const response = await fetch(`http://localhost:5000/leaderboard?game=${selectedGame}`);
        const data = await response.json();
        setPlayers(data);
      } catch (err) {
        console.error('Failed to fetch leaderboard:', err);
      }
    };

    fetchLeaderboard();
    const interval = setInterval(fetchLeaderboard, 3000);
    return () => clearInterval(interval);
  }, [selectedGame]);

  return (
    <div style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Real-Time Leaderboard</h1>

      <label htmlFor="game-select">Select Game: </label>
      <select
        id="game-select"
        value={selectedGame}
        onChange={(e) => setSelectedGame(e.target.value)}
      >
        {games.map((game) => (
          <option key={game} value={game}>
            {game}
          </option>
        ))}
      </select>

      <table border="1" cellPadding="10" cellSpacing="0" style={{ marginTop: '20px' }}>
        <thead>
          <tr>
            <th>Rank</th>
            <th>Player</th>
            <th>Kills</th>
            <th>Deaths</th>
            <th>Items</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          {players.map((player, index) => (
            <tr key={player.player_id}>
              <td>{index + 1}</td>
              <td>{player.player_id}</td>
              <td>{player.kills}</td>
              <td>{player.deaths}</td>
              <td>{player.items}</td>
              <td>{player.score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;

