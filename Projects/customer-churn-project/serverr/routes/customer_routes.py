from flask import Blueprint
from controllers.customer_controller import (
    fetch_all_customers,
    fetch_customer_by_id,
    fetch_customers_by_contract,
    fetch_customers_paginated
)

# Create Blueprint
customer_bp = Blueprint("customer_bp", __name__)

# Get all customers
customer_bp.route("/customers", methods=["GET"])(fetch_all_customers)

# Get customer by ID
customer_bp.route("/customers/search", methods=["GET"])(fetch_customer_by_id)

# Filter by contract
customer_bp.route("/customers/filter", methods=["GET"])(fetch_customers_by_contract)

# Pagination
customer_bp.route("/customers/paginate", methods=["GET"])(fetch_customers_paginated)