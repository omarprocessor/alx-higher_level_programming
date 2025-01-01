#!/usr/bin/python3
"""
4-cities_by_state.py

This script lists all cities from the database `hbtn_0e_4_usa`,
 sorted by city ID.
It takes in 3 arguments: MySQL username, MySQL password, and database name.
It uses MySQLdb to connect to the database, and results are
 displayed in the format:
(city_id, city_name, state_name)
"""

import sys
import MySQLdb


def list_cities(username, password, database):
    """
    Lists all cities from the `cities` table of the `hbtn_0e_4_usa` database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

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

        # Use a single query to join `cities` and `states` tables
        # and sort by city ID
        query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """
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
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
