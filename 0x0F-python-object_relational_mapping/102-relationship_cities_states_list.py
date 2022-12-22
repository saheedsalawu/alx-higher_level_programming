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

    all_cities = session.query(City).order_by(City.id)

    for ct in all_cities:
        print("{}: {} -> {}".format(ct.id, ct.name, ct.state.name))
    session.close()
