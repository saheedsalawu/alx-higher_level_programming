#!/usr/bin/python3

"""
This is a script that  prints all City
objects from the database hbtn_0e_14_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker()
    session = Session(bind=engine)

    all_city = session.query(City).order_by(City.id)
    all_state = session.query(State).order_by(State.id)

    for inst in all_city:
        for st in all_state:
            if (st.id == inst.state_id):
                print('{}: ({}) {}'.format(st.name, inst.id, inst.name))
    session.close()
