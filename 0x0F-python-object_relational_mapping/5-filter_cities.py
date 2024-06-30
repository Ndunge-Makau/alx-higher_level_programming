#!/usr/bin/python3

"""Takes in the name of a state as an argument
    - and lists all cities of that state,
    - using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect("localhost", argv[1], '', argv[3], port=3306)
    cur = db.cursor()
    my_state = argv[4]
    cur.execute("SELECT cities.name\
                FROM cities INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name LIKE %s", (my_state, ))
    rows = cur.fetchall()
    count = 1
    for row in rows:
        if row:
            print(row[0], end='')
            if count != len(rows):
                print(", ", end='')
        count += 1
    print()
