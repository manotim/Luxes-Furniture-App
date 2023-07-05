// import React from 'react'

// function updateFurniture() {
//   return (
//     <div>
//       <div className="App">
//       {furniture.map(furnitureItem => (
//         <div key={furnitureItem.id}>
//           <img src={furnitureItem.image} alt={furnitureItem.name} />
//           <h2>{furnitureItem.name}</h2>
//           <p>{furnitureItem.description}</p>
//         </div>
//       ))}
//     </div>
//     </div>
//   )
// }

// export default updateFurniture
import React, { useState } from 'react';

function UpdateFurniture({ furniture, onUpdateFurniture }) {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [image, setImage] = useState('');

  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  const handleDescriptionChange = (event) => {
    setDescription(event.target.value);
  };

  const handleImageChange = (event) => {
    setImage(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    // Find the furniture item to update
    const furnitureToUpdate = furniture.find((furnitureItem) => {
      // Assuming the furniture has a unique identifier 'id'
      return furnitureItem.id === selectedFurnitureId;
    });

    if (furnitureToUpdate) {
      // Create an updated furniture object
      const updatedFurniture = {
        ...furnitureToUpdate,
        name: name || furnitureToUpdate.name,
        description: description || furnitureToUpdate.description,
        image: image || furnitureToUpdate.image,
      };

      // Call the onUpdateFurniture callback with the updated furniture object
      onUpdateFurniture(updatedFurniture);
    }

    // Reset the form inputs
    setName('');
    setDescription('');
    setImage('');
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            value={name}
            onChange={handleNameChange}
          />
        </div>
        <div>
          <label htmlFor="description">Description:</label>
          <input
            type="text"
            id="description"
            value={description}
            onChange={handleDescriptionChange}
          />
        </div>
        <div>
          <label htmlFor="image">Image URL:</label>
          <input
            type="text"
            id="image"
            value={image}
            onChange={handleImageChange}
          />
        </div>
        <button type="submit">Update Furniture</button>
      </form>
    </div>
  );
}

export default UpdateFurniture;
