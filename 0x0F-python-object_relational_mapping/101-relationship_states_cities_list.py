#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    # Ensure the correct number of arguments are passed
    if len(sys.argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py")
        print("       mysql_username mysql_password database_name")
        sys.exit(1)

    # Get arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Create the engine and session
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}'
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states and their corresponding cities in ascending order
    states = session.query(State).join(City).order_by(State.id, City.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    # Close the session
    session.close()
