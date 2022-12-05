#!/usr/bin/python3
"""
Script  prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    name = "Louisiana"
    Session = sessionmaker(engine)
    session = Session()
    state = State(name=name)
    session.add(state)
    session.commit()
    state = session.query(State).filter_by(name=name).first()
    print(state.id)
    session.close()
