#!/usr/bin/python3
"""
1-filter_states.py

This script lists all states from the database `hbtn_0e_0_usa`
with names starting with 'N' (upper N).
It connects to a MySQL server running on localhost at port 3306
using provided user credentials and retrieves matching states
sorted by `id` in ascending order.

Usage:
    ./1-filter_states.py <mysql_username> <mysql_password> <database_name>

Example:
    ./1-filter_states.py root root hbtn_0e_0_usa
"""

import MySQLdb
import sys


def filter_states_by_n(username, password, database):
    """
    Connects to the MySQL database and retrieves states
    with names starting with 'N'.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database.

    Returns:
        None
    """
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

        results = cursor.fetchall()
        for row in results:
            print(row)

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 4:
        filter_states_by_n(sys.argv[1], sys.argv[2], sys.argv[3])
