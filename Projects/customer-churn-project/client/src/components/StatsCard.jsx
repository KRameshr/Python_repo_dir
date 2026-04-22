import React from "react";

const StatsCard = ({ title, value, color = "primary" }) => {
  return (
    <div className="card shadow-sm border-0 p-3 h-100">
      <small className="text-muted fw-bold text-uppercase">{title}</small>

      <div className={`h2 fw-bold text-${color} mb-0`}>{value}</div>
    </div>
  );
};

export default StatsCard;
