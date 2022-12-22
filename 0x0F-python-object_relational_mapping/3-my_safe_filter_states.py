#!/usr/bin/python3

"""
a script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
But this time, this one is safe from MySQL injections!
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
            """SELECT *
            FROM states
            WHERE name='{}'
            ORDER BY id ASC
            """.format(arg[4])
            )
    state_rows = cur.fetchall()
    for state in state_rows:
        if (state[1] == arg[4]):
            print(state)
    cur.close()
    conn.close()
