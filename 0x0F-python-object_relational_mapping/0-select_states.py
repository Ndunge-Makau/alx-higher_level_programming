#!/usr/bin/python3

"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect("localhost", argv[1], '', argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT id, name\
                FROM states\
                ORDER BY id")
    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()
