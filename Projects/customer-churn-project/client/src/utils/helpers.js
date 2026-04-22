export const calculateStats = (customers) => {
  const total = customers.length;

  const churned = customers.filter((c) => c.Churn === "Yes").length;

  const retention =
    total > 0 ? (((total - churned) / total) * 100).toFixed(1) : 0;

  const avgCharge =
    total > 0
      ? (
          customers.reduce(
            (acc, curr) => acc + (parseFloat(curr.MonthlyCharges) || 0),
            0,
          ) / total
        ).toFixed(2)
      : 0;

  return { total, churned, retention, avgCharge };
};
