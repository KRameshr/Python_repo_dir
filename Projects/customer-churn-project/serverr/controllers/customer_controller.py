from flask import request, jsonify
from utils.helper import success_response, error_response, get_pagination_params
from services.customer_service import (
    fetch_all_customers_service,
    fetch_customer_by_id_service,
    fetch_customers_by_contract_service,
    fetch_customers_paginated_service
)

# Get all
def fetch_all_customers():
    data = fetch_all_customers_service()
    return success_response(data)


# Get by ID
def fetch_customer_by_id():
    customer_id = request.args.get("id")
    if not customer_id:
        return error_response("Customer ID is required", 400)
    data, status = fetch_customer_by_id_service(customer_id)
    if status != 200:
        return error_response(data.get("message", "Not Found"), status) 
    return success_response(data)


# Filter
def fetch_customers_by_contract():
    contract = request.args.get("contract")
    if not contract:
        return error_response("Contract type is required", 400)
    data, status = fetch_customers_by_contract_service(contract)
    return success_response(data)


# Pagination
def fetch_customers_paginated():
    limit, offset = get_pagination_params(request)
    data, status = fetch_customers_paginated_service(limit, offset)
    
    if status != 200:
        msg = data.get("error") if isinstance(data, dict) else "Pagination failed"
        return error_response(msg, status)
    return success_response(data)