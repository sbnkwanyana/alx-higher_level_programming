#!/usr/bin/python3
"""
Connects using SQLAlchemy to retrive all states that contain the letter 'a'
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

    Session = sessionmaker(engine)
    session = Session()
    state = session.query(State).first()
    for state in session.query(
                               State).filter(
                               State.name.like('%a%')).order_by(
                               State.id).all():
        print(f"{state.id}: {state.name}")
    session.close()
