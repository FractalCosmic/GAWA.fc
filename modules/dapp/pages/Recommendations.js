// pages/Recommendations.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Recommendations() {
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    const fetchRecommendations = async () => {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.post('http://localhost:5000/recommend', 
          { preferences: 'user preferences' },  // 这里应该是用户的实际偏好
          { headers: { Authorization: `Bearer ${token}` } }
        );
        setRecommendations(response.data);
      } catch (error) {
        console.error('Failed to fetch recommendations', error);
      }
    };

    fetchRecommendations();
  }, []);

  return (
    <div>
      <h2>Your Recommendations</h2>
      <ul>
        {recommendations.map((item, index) => (
          <li key={index}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default Recommendations;
