import React from "react";
import Dashboard from "./pages/Dashboard";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
  return (
    <div className="min-vh-100 bg-light">
      <nav className="navbar navbar-dark bg-dark mb-4">
        <div className="container">
          <span className="navbar-brand">
            Customer Churn Analytics Dashboard
          </span>
        </div>
      </nav>

      <div className="container">
        <Dashboard />
      </div>
    </div>
  );
}

export default App;
