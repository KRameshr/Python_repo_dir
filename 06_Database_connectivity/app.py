import mysql.connector

# Database connection config
config = {
    "host": "localhost",
    "user": "root",
    "password": "Ramesh@2002",
    "database":"intell"
}

try:
    mydb = mysql.connector.connect(**config)

    if mydb.is_connected():
        cursor = mydb.cursor()
        print("--- Connected to MySQL Server ---\n")

        # cursor.execute("SHOW DATABASES")
        # print("List of Databases:\n")
        
        cursor.execute("SHOW tables")
        print("List of tables:\n")
        for db in cursor:
            print(db[0])

        # insert_query = """
        # INSERT INTO employee (name, department, salary, hire_date)
        # VALUES (%s, %s, %s, %s)
        # """
        # data = ("Ramesh", "IT", 50000, "2024-01-10")
        # cursor.execute(insert_query, data)
        # mydb.commit() #is permanet is data

        # insert_query = """
        # INSERT INTO employee (name, department, salary, hire_date)
        # VALUES (%s, %s, %s, %s)
        # """
        # data = [
        #     ("Suresh", "HR", 40000, "2023-05-15"),
        #     ("Anita", "Finance", 55000, "2022-11-20"),
        #     ("Kiran", "IT", 60000, "2021-08-10"),
        #     ("Priya", "Marketing", 45000, "2023-02-25")
        #     ]
        # cursor.executemany(insert_query, data)
        # mydb.commit()
        # print(cursor.rowcount, "records inserted")

        # delete_query = "DELETE FROM employee WHERE name = %s"
        # data = ("Suresh",)
        # cursor.execute(delete_query, data)
        # mydb.commit()
        # print(cursor.rowcount, "record(s) deleted")


        update_query = "UPDATE employee SET name = %s WHERE name = %s"
        data = ("Ramesh", "Usha")  # update_Value # previous_Value
        cursor.execute(update_query, data)
        mydb.commit()
        print(cursor.rowcount, "record(s) updated")

        # Show employee data
        cursor.execute("SELECT * FROM employee")
        print("\n Employee Data:\n")
        for row in cursor.fetchall():
            print(row)

            


    print(f"{cursor.rowcount} record inserted successfully")

except mysql.connector.Error as err:
    print(f"MySQL Error: {err}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("\n--- Connection Closed Safely ---")