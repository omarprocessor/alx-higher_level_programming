#!/usr/bin/python3
import MySQLdb
import sys

"""
This script lists all cities of a given state from a MySQL database.

Usage:
    ./5-filter_cities.py <mysql_username> <mysql_password> <database_name>
    <state_name>

Arguments:
    mysql_username (str): The MySQL username.
    mysql_password (str): The MySQL password.
    database_name (str): The name of the MySQL database.
    state_name (str): The name of the state whose cities are to be listed.

Description:
    This script connects to a MySQL
database, executes a query to retrieve the cities
    of the given state, sorts the cities by their ID in ascending
order, and prints
    the names of the cities in a comma-separated format.

    The script uses parameterized queries to prevent SQL injection.

Requirements:
    - The MySQLdb module must be installed.
    - The script must be executed on a server running MySQL on localhost at
port 3306.
"""

if __name__ == "__main__":
    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to execute the query
    cursor = db.cursor()

    # Execute the query to retrieve cities for the given state
    cursor.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    # Fetch all results
    cities = cursor.fetchall()

    # Display results, joined by commas
    if cities:
        print(", ".join(city[0] for city in cities))

    # Close the cursor and database connection
    cursor.close()
    db.close()
