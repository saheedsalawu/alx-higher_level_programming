#!/usr/bin/python3

"""
This is  a script that takes in an argument and
displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
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
            """SELECT *
            FROM states
            WHERE name='{}'
            ORDER BY id ASC""".format(arg[4])
            )
    state_rows = cur.fetchall()
    for state in state_rows:
        if (state[1] == arg[4]):
            print(state)
    cur.close()
    conn.close()
