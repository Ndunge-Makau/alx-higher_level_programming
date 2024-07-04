#!/usr/bin/python3

"""Lists all City objects from the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_city import City
from relationship_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], '',
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    my_query = session.query(State).order_by(State.id)
    for state in my_query:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
