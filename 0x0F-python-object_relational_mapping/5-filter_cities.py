#!/usr/bin/python3

"""
This is a script that takes in the name
of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa
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
    if "'" in arg[4]:
        idx = arg[4].index("'")
        arg[4] = arg[4][:idx]
    cur.execute(
            """SELECT cities.name
            FROM cities
            INNER JOIN states ON states.id = cities.state_id
            WHERE states.name = '{}'
            ORDER BY cities.id ASC""".format(arg[4])
            )
    city_rows = cur.fetchall()
    for i in range(len(city_rows)):
        print(city_rows[i][0], end='')
        if (i != len(city_rows) - 1):
            print(', ', end='')
        else:
            print('')
    cur.close()
    conn.close()
