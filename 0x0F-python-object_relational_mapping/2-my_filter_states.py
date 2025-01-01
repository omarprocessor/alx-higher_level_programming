#!/usr/bin/python3
"""
2-my_filter_states.py

This script takes in an argument and displays all values in the
`states` table of the database `hbtn_0e_0_usa` where `name` matches
the argument. The results are sorted in ascending order by `id`.

Usage:
    ./2-my_filter_states.py <mysql_username>
 <mysql_password> <database_name> <state_name>
"""

import sys
import MySQLdb


def filter_states_by_name(username, password, database, state_name):
    """
    Connects to the MySQL database and retrieves states where the name matches
    the provided state_name argument.

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
        query = (
            "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
            .format(state_name)
        )
        cursor.execute(query)

        results = cursor.fetchall()
        for row in results:
            print(row)

        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) == 5:
        filter_states_by_name(
            sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
        )
