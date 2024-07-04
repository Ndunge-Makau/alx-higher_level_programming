#!/usr/bin/python3

"""Creates the State “California” with the City “San Francisco”
    from the database hbtn_0e_100_usa:
    (100-relationship_states_cities.py)"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], '',
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)

    California = State(name="California")
    San_Francisco = City(name="San Francisco")
    California.cities.append(San_Francisco)

    session.add(California)
    session.add(San_Francisco)
    session.commit()
