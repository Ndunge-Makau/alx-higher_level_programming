#!/usr/bin/python3

"""Takes in arguments and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections!"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()
    my_state = argv[4]
    cur.execute("SELECT * FROM states\
            WHERE name LIKE %s", (my_state, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
