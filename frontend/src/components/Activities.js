import React, { useEffect, useState } from 'react';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'https://miniature-parakeet-5vr54x94x66f7pqg-8000.app.github.dev';

function Activities() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetch(`${API_BASE_URL}/api/activities/`)
      .then(response => response.json())
      .then(data => setActivities(data))
      .catch(error => console.error('Error fetching activities:', error));
  }, []);

  return (
    <div className="container mt-4">
      <h1 className="text-center text-primary">Activities</h1>
      <table className="table table-striped table-bordered mt-4">
        <thead className="table-dark">
          <tr>
            <th>Activity Type</th>
            <th>Duration</th>
          </tr>
        </thead>
        <tbody>
          {activities.map(activity => (
            <tr key={activity._id}>
              <td>{activity.activity_type}</td>
              <td>{activity.duration}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Activities;
