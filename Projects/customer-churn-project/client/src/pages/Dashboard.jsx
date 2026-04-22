import React, { useState, useMemo } from "react";
import { useCustomers } from "../hooks/useCustomers";
import { calculateStats } from "../utils/helpers";

import CustomerTable from "../components/CustomerTable";
import StatsCard from "../components/StatsCard";
import SearchBar from "../components/SearchBar";

const Dashboard = () => {
  const { customers, loading, error, reload } = useCustomers();
  const [searchTerm, setSearchTerm] = useState("");

  // Filter logic
  const filteredCustomers = useMemo(() => {
    return customers.filter((c) =>
      c.customerID?.toLowerCase().includes(searchTerm.toLowerCase()),
    );
  }, [customers, searchTerm]);

  // Stats
  const { total, churned, retention, avgCharge } = calculateStats(customers);

  // Loading UI
  if (loading) {
    return (
      <div className="d-flex justify-content-center align-items-center vh-100">
        <div className="spinner-border text-primary"></div>
      </div>
    );
  }

  return (
    <div className="container-xl py-4">
      {/* HEADER */}
      <div className="d-flex justify-content-between mb-4">
        <h2>Dashboard</h2>
        <SearchBar value={searchTerm} onChange={setSearchTerm} />
      </div>

      {/* ERROR */}
      {error && <div className="alert alert-danger text-center">{error}</div>}

      {/* STATS */}
      <div className="row g-3 mb-4">
        <div className="col-md-3">
          <StatsCard title="Total Clients" value={total} />
        </div>
        <div className="col-md-3">
          <StatsCard title="Churned" value={churned} color="danger" />
        </div>
        <div className="col-md-3">
          <StatsCard
            title="Retention"
            value={`${retention}%`}
            color="success"
          />
        </div>
        <div className="col-md-3">
          <StatsCard title="Avg Revenue" value={`$${avgCharge}`} color="dark" />
        </div>
      </div>

      {/* TABLE */}
      <CustomerTable customers={filteredCustomers} />
    </div>
  );
};

export default Dashboard;
