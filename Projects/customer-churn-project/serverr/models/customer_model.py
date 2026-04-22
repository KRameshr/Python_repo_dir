from config.db import get_db_connection

# Get all customers
def get_all_customers():
    conn = get_db_connection()
    if not conn:
        return []   
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customer_churn")
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(f"Error fetching all customers: {e}")
        return []
    finally:
        if 'cursor' in locals(): cursor.close()
        conn.close()


# Get customer by ID
def get_customer_by_id(customer_id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM customer_churn WHERE customerID LIKE %s"
        cursor.execute(query, (f"%{customer_id}%",)) 
        data = cursor.fetchone()
        return data
    finally:
        cursor.close()
        conn.close()

# Get customers by Contract (Filter)
def get_customers_by_contract(contract):
    conn = get_db_connection()
    if not conn:
        return []
    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM customer_churn WHERE Contract = %s"
        cursor.execute(query, (contract,))
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(f"❌ Error filtering by contract: {e}")
        return []
    finally:
        if 'cursor' in locals(): cursor.close()
        conn.close()


# Pagination (limit + offset)
def get_customers_paginated(limit, offset):
    conn = get_db_connection()
    if not conn:
        return []
    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM customer_churn LIMIT %s OFFSET %s"
        cursor.execute(query, (int(limit), int(offset)))
        data = cursor.fetchall()
        return data
    except Exception as e:
        print(f"Error during pagination: {e}")
        return []
    finally:
        if 'cursor' in locals(): cursor.close()
        conn.close()