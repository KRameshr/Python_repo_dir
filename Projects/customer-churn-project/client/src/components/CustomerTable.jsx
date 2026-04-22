import React from "react";

const CustomerTable = ({ customers }) => {
  return (
    <div className="card shadow-sm border-0">
      <div className="table-responsive">
        <table className="table table-hover align-middle mb-0">
          <thead className="table-light">
            <tr className="text-secondary text-uppercase small">
              <th className="px-4 py-3">Customer ID</th>
              <th className="py-3">Contract Type</th>
              <th className="py-3 text-center">Monthly Charges</th>
              <th className="py-3 text-center">Status</th>
            </tr>
          </thead>

          <tbody>
            {customers && customers.length > 0 ? (
              customers.map((c) => {
                const charge = Number(c.MonthlyCharges) || 0;

                return (
                  <tr key={c.customerID}>
                    <td className="px-4 py-3 fw-bold text-primary">
                      {c.customerID}
                    </td>

                    <td className="py-3">
                      <span className="text-dark">{c.Contract}</span>
                    </td>

                    <td className="py-3 text-center fw-medium">
                      ${charge.toFixed(2)}
                    </td>

                    <td className="py-3 text-center">
                      <span
                        className={`badge rounded-pill px-3 py-2 ${
                          c.Churn === "Yes"
                            ? "bg-danger-subtle text-danger"
                            : "bg-success-subtle text-success"
                        }`}
                        style={{ border: "1px solid currentColor" }}
                      >
                        {c.Churn === "Yes" ? "Churned" : "Active Member"}
                      </span>
                    </td>
                  </tr>
                );
              })
            ) : (
              <tr>
                <td colSpan="4" className="text-center py-5 text-muted">
                  No customers found.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default CustomerTable;
