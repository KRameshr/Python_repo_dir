# Customer Churn Analytics Dashboard

A full-stack web application to analyze customer churn data using a modern architecture with Flask (Backend) and React (Frontend).

---

## Features

- View all customer records
- Search customers by ID
- Real-time churn analytics (Retention, Churn Rate, Revenue)
- Pagination support
- Filter customers by contract type
- Responsive UI with Bootstrap
- Secure backend using environment variables (.env)

---

## Tech Stack

### Frontend

- React (Hooks + Component-Based Architecture)
- Axios (API calls)
- Bootstrap (UI styling)

### Backend

- Flask (REST API)
- MySQL (Database)
- MVC Architecture (Controller, Service, Model)
- Flask-CORS

---
````
## Project Structure

customer-churn-project/
│
├── server/ ← Python Backend (Flask MVC)
│ │
│ ├── app.py
│ │
│ ├── config/
│ │ └── db.py
│ │
│ ├── models/
│ │ └── customer_model.py
│ │
│ ├── controllers/
│ │ └── customer_controller.py
│ │
│ ├── routes/
│ │ └── customer_routes.py
│ │
│ ├── services/ ← business logic
│ │ └── customer_service.py
│ │
│ ├── utils/ ← helpers
│ │ └── helpers.py
│ │
│ ├── tests/
│ │ └── test_customer.py
│ │
│ └── requirements.txt
│
├── client/ ← React Frontend
│ │
│ src/
│ │
│ ├── components/ # UI (dumb components)
│ │ ├── CustomerTable.jsx
│ │ ├── StatsCard.jsx
│ │ ├── SearchBar.jsx
│ │
│ ├── pages/ # Page-level (smart components)
│ │ └── Dashboard.jsx
│ │
│ ├── hooks/ # Business logic (like controllers)
│ │ └── useCustomers.js
│ │
│ ├── services/ # API layer
│ │ └── api.js
│ │
│ ├── utils/ # Helpers
│ │ └── helpers.js
│ │
│ ├── App.jsx
│ └── main.jsx
│
└── README.md let build fronted step by step react
```
