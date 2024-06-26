#!/usr/bin/python3

"""Prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    my_query = session.query(State).filter_by(name=sys.argv[4]).first()

    if my_query is None:
        print("Not found")
    else:
        print(my_query.id)
