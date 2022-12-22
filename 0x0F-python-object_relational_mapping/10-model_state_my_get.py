#!/usr/bin/python3

"""
This is a a script that prints the
State object with the name passed as
argument from the database hbtn_0e_6_usa
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

    a = 1
    state_filter = session.query(State).filter_by(name=sys.argv[4])
    for inst in state_filter:
        a = 0
        print(inst.id)
    if a:
        print('Not found')
    session.close()
