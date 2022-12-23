#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
and the cities
from the database `hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("SELECT cities.id, cities.name, \
                    states.name FROM states JOIN cities\
                    ON cities.state_id = states.id \
                    ORDER BY cities.id ASC")

        numrows = cur.fetchall()

    if numrows is not None:
        for item in numrows:
            print(item)
