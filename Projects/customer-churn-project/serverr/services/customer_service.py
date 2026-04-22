from models.customer_model import (
    get_all_customers,
    get_customer_by_id,
    get_customers_by_contract,
    get_customers_paginated
)

#  Get all customers
def fetch_all_customers_service():
    return get_all_customers()


#  Get customer by ID
def fetch_customer_by_id_service(customer_id):
    if not customer_id:
        return {"error": "Customer ID is required"}, 400
    data = get_customer_by_id(customer_id)
    if not data:
        return {"message": "Customer not found"}, 404
    return data, 200


#  Filter by contract
def fetch_customers_by_contract_service(contract):
    if not contract:
        return {"error": "Contract is required"}, 400
    data = get_customers_by_contract(contract)
    return data, 200


#  Pagination
def fetch_customers_paginated_service(limit, offset):
    try:
        limit = int(limit)
        offset = int(offset)
    except ValueError:
        return {"error": "Invalid limit or offset"}, 400
    data = get_customers_paginated(limit, offset)
    return data, 200