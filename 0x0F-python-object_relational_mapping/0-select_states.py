#!/usr/bin/python3
import MySQLdb
import sys

def main():
    # Step 1: Retrieve arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Step 2: Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Step 3: Create a cursor object to interact with the database
    cursor = db.cursor()

    # Step 4: Execute the query to fetch all states
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Step 5: Fetch all rows from the query
    rows = cursor.fetchall()

    # Step 6: Print each row in the required format
    for row in rows:
        print(row)

    # Step 7: Close the cursor and connection
    cursor.close()
    db.close()

# Step 8: Ensure that the script runs only when executed directly
if __name__ == "__main__":
    main()
