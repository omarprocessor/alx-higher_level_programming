#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    # Ensure the correct number of arguments are passed
    if len(sys.argv) != 4:
        print("Usage: ./100-relationship_states_citiespassword database_name")
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

    # Create the state and city
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)

    # Add the new state and city to the session and commit to the database
    session.add(california)
    session.add(san_francisco)
    session.commit()

    # Close the session
    session.close()
