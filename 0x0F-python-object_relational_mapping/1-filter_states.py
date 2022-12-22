#!/usr/bin/python3
"""This script
lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    """
    Access the database and get the states
    with name starting with Upper N.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    numrows = cur.fetchall()

    for item in numrows:
        print(item)
