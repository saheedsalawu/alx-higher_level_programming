#!/usr/bin/python3

"""
This is  a script that lists all cities
from the database hbtn_0e_4_usa
"""


import MySQLdb
import sys

if __name__ == "__main__":
    arg = sys.argv
    conn = MySQLdb.connect(
        host="localhost",
        port=3306, user=arg[1],
        passwd=arg[2], db=arg[3],
        charset="utf8"
        )
    cur = conn.cursor()
    cur.execute(
            """SELECT cities.id,
                cities.name,
                states.name
            FROM cities
            INNER JOIN states ON states.id = cities.state_id
            ORDER BY cities.id ASC"""
            )
    city_rows = cur.fetchall()
    for city in city_rows:
        print(city)
    cur.close()
    conn.close()
