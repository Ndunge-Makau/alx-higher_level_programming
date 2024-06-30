#!/usr/bin/python3

"""Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name LIKE BINARY 'N%'\
                ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
