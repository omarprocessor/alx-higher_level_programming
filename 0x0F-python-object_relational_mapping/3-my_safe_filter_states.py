#!/usr/bin/python3
"""
3-my_safe_filter_states.py

This script takes in arguments and displays all values in the `states`
table of the database `hbtn_0e_0_usa` where `name` matches the argument.
The script is safe from MySQL injections.

Usage:
    ./3-my_safe_filter_states.py
 <mysql_username> <mysql_password> <database_name> <state_name>
"""

import sys
import MySQLdb


def safe_filter_states_by_name(username, password, database, state_name):
    """
    Connects to the MySQL database and retrieves states where the name matches
    the provided state_name argument. Prevents SQL injection.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database.
        state_name (str): The state name to filter by.

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
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        results = cursor.fetchall()
        for row in results:
            print(row)

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 5:
        safe_filter_states_by_name(
            sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        )
