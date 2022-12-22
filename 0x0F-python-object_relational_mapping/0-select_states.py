#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="Davoko0987*", db="hbtn_0e_0_usa")

cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY id ASC")
for item in cur:
    print(cur.fetchone())
