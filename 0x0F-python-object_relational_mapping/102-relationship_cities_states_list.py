#!/usr/bin/python3
"""
Lists all City objects and corresponding State objects from the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State
from base import Base
import sys


def list_cities_states(username, password, db_name):
    """Lists all cities and their corresponding states from the database."""

    # Create engine and session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query cities and their related states
    cities = session.query(City).order_by(City.id).all()

    # Output the results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close session
    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./102-relationship_cities_states_list.py "
              "mysql_username mysql_password database_name")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    list_cities_states(username, password, db_name)
