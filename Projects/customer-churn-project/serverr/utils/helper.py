from flask import jsonify

# Standard success response
def success_response(data, message="Success", status=200):
    return jsonify({
        "status": "success",
        "message": message,
        "data": data
    }), status


# Standard error response
def error_response(message="Error", status=400):
    return jsonify({
        "status": "error",
        "message": message
    }), status


# Validate required query parameter
def validate_param(param, param_name):
    if not param:
        return False, f"{param_name} is required"
    return True, None


# Convert string to int safely
def parse_int(value, default=0):
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


# Pagination helper
def get_pagination_params(request):
    limit = parse_int(request.args.get("limit", 50))
    offset = parse_int(request.args.get("offset", 0))
    return limit, offset