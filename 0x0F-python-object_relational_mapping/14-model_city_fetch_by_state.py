#!/usr/bin/python3
"""
Returns all cities with their states and id
"""


from model_state import Base, State
from model_city import City
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for result in session.query(State.name,
                                City.id,
                                City.name).order_by(City.id).filter(
                                              State.id == City.state_id):
        print(f'{result[0]}: ({result[1]}) {result[2]}')
    session.close()
