import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('http://127.0.0.1:8000')
      .then(response => {
        setMessage(response.data.message);
      })
      .catch(error => {
        console.error("Error fetching data from backend.", error);
        setMessage('Error fetching data from backend.');
      });
  }, []);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/${studentName}')
      .then(response => {
        setMessage(response.data.message);
      })
      .catch(error => {
        console.error("Error fetching data from backend for students.", error);
        setMessage('Error fetching data from backend.');
      });
  }, []);

  return (
    <div>
      <h1>Student Data Visualization</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;
