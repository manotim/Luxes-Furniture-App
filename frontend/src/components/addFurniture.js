import React, { useState } from 'react';

function AddFurniture({ onAddFurniture }) {
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

    // Create a new furniture object
    const newFurniture = {
      name,
      description,
      image,
    };

    // Call the onAddFurniture callback with the new furniture object
    onAddFurniture(newFurniture);

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
            required
          />
        </div>
        <div>
          <label htmlFor="description">Description:</label>
          <input
            type="text"
            id="description"
            value={description}
            onChange={handleDescriptionChange}
            required
          />
        </div>
        <div>
          <label htmlFor="image">Image URL:</label>
          <input
            type="text"
            id="image"
            value={image}
            onChange={handleImageChange}
            required
          />
        </div>
        <button type="submit">Add Furniture</button>
      </form>
    </div>
  );
}

export default AddFurniture;
