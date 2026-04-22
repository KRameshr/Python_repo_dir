import React from "react";

const SearchBar = ({ value, onChange }) => {
  return (
    <input
      type="text"
      className="form-control shadow-sm border-0"
      placeholder="Search Customer ID..."
      value={value}
      onChange={(e) => onChange(e.target.value)}
      style={{ minWidth: "200px" }}
    />
  );
};

export default SearchBar;
