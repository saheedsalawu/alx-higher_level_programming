#!/usr/bin/python3

"""
This is a script that changes the name
of a State object from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker()
    session = Session(bind=engine)

    to_update = session.query(State).filter_by(id=2)

    if to_update[0]:
        to_update[0].name = 'New Mexico'
        session.add(to_update[0])
        session.commit()
    session.close()
