#!/usr/bin/python3

"""Prints all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine, update
from sqlalchemy.orm import Session
from model_city import City
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    my_query = session.query(City.name, City.id, State.name).\
        join(State, City.state_id == State.id).all()
    for city in my_query:
        print("{}: ({}) {}".format(city[2], city[1], city[0]))
