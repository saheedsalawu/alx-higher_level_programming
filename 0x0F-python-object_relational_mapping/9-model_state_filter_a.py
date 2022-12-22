#!/usr/bin/python3

"""
This is a script that lists all State
objects that contain the letter a from
the database hbtn_0e_6_usa
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

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).order_by(State.id)
    for inst in all_states:
        if 'a' in inst.name:
            print("{}: {}".format(inst.id, inst.name))
    session.close()
