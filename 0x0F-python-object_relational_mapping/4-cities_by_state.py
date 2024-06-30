#!/usr/bin/python3

"""Lists all cities from the database hbtn_0e_4_usa."""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect("localhost", argv[1], '', argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
             FROM cities INNER JOIN states\
             ON cities.state_id = states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
