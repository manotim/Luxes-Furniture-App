import React from 'react'

function updateFurniture() {
  return (
    <div>
      <div className="App">
      {furniture.map(furnitureItem => (
        <div key={furnitureItem.id}>
          <img src={furnitureItem.image} alt={furnitureItem.name} />
          <h2>{furnitureItem.name}</h2>
          <p>{furnitureItem.description}</p>
        </div>
      ))}
    </div>
    </div>
  )
}

export default updateFurniture
