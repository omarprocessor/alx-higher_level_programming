#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

import sys

if __name__ == "__main__":
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

    # Query the cities and their related states
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Print the results
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()
