#!/usr/bin/python3
"""
0-select_states.py

This script lists all states from the database `hbtn_0e_0_usa`.
It connects to a MySQL server running on localhost at port 3306 using
provided user credentials and retrieves states sorted by `id` in
ascending order.

Usage:
    ./0-select_states.py <mysql_username> <mysql_password> <database_name>

Example:
    ./0-select_states.py root root hbtn_0e_0_usa
"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    Connects to the MySQL database and retrieves all states sorted by id.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database.

    Returns:
        None
    """
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()

        # Execute the query to retrieve all states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch and print all results
        results = cursor.fetchall()
        for row in results:
            print(row)

        # Close cursor and connection
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    # Ensure the script is not executed when imported
    if len(sys.argv) == 4:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
