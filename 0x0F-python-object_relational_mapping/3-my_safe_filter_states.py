#!/usr/bin/python3

"""Takes in arguments and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.
    But this time, write one that is safe from MySQL injections!"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect("localhost", argv[1], '', argv[3], port=3306)
    cur = db.cursor()
    if len(argv) == 5:
        cur.execute("SELECT * FROM states\
                    WHERE name LIKE BINARY '{}'".format(argv[4]))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    cur.close()
    db.close()
