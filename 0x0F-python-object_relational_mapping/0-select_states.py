#!/usr/bin/python3
"""script that lists all states
from the database hbtn_0e_0_usa
"""
import MySQLdb


if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user="root",
                         passwd="Davoko0987*", db="hbtn_0e_0_usa")

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for item in cur:
        print(cur.fetchone())
