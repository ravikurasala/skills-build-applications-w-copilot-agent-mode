import React, { useEffect, useState } from 'react';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'https://miniature-parakeet-5vr54x94x66f7pqg-8000.app.github.dev';

function Leaderboard() {
  const [leaderboard, setLeaderboard] = useState([]);

  useEffect(() => {
    fetch(`${API_BASE_URL}/api/leaderboard/`)
      .then(response => response.json())
      .then(data => setLeaderboard(data))
      .catch(error => console.error('Error fetching leaderboard:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center text-primary">Leaderboard</h1>
      <table className="table table-striped table-bordered mt-4">
        <thead className="table-dark">
          <tr>
            <th>Username</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          {leaderboard.map(entry => (
            <tr key={entry._id}>
              <td>{entry.user.username}</td>
              <td>{entry.score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Leaderboard;
