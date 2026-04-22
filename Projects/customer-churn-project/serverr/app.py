from flask import Flask, jsonify
from flask_cors import CORS
from routes.customer_routes import customer_bp

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

@app.route("/")
def index():
    return jsonify({
        "status": "success",
        "message": "Customer Churn API is active",
        "endpoints": ["/api/customers", "/api/customers/search", "/api/customers/paginate"]
    })
app.register_blueprint(customer_bp, url_prefix="/api")

@app.errorhandler(404)
def resource_not_found(e):
    return jsonify({
        "status": "error",
        "message": "URL not found. Remember to include the '/api' prefix for data routes.",
    }), 404


with app.app_context():
    print("\n--- API SERVER STARTING ---")
    for rule in app.url_map.iter_rules():
        print(f"URL: {rule}")
    print("---------------------------\n")

if __name__ == "__main__":
    app.run(debug=True, port=5000)