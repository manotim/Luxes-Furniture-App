import React, { useState, useEffect } from 'react';

import './App.css';
import AddFurniture from './components/addFurniture';

function App() {
  const [furniture, setFurniture] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/furnitures')
      .then(resp => resp.json())
      .then(data => setFurniture(data)) 
      .catch(error => console.error(error));
  }, []);

  return (
    <div className="App">
      <AddFurniture/>
      {furniture.map(furnitureItem => (
        <div key={furnitureItem.id}>
          <img src={furnitureItem.image} alt={furnitureItem.name} />
          <h2>{furnitureItem.name}</h2>
          <p>{furnitureItem.description}</p>
        </div>
      ))}
    </div>
  );
}

export default App;
