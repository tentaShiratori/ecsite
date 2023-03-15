export function Create() {
  return (
    <div>
      <div>
        <label htmlFor="name">Name</label>
        <input type="text" />
      </div>
      <div>
        <label htmlFor="description">Description</label>
        <input type="text" />
      </div>
      <div>
        <label htmlFor="price">Price</label>
        <input type="text" />
      </div>
      <div>
        <label htmlFor="image">Image</label>
        <input type="file" />
      </div>
    </div>
  );
}
