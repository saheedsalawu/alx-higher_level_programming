#!/usr/bin/python3

"""
This is a script that  prints all City
objects from the database hbtn_0e_14_usa
"""


import sys
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker()
    session = Session(bind=engine)

    all_state = session.query(State).order_by(State.id)

    for st in all_state:
        print("{}: {}".format(st.id, st.name))
        for ct in st.cities:
            print("    {}: {}".format(ct.id, ct.name))
    session.close()
