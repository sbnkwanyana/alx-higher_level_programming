#!/usr/bin/python3
"""Module connects to database using MySQLdb client using values passed
through command line arguments to select states that match their start
with given value"""

import sys
import MySQLdb

if __name__ == "__main__":
    host = 'localhost'
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=database, charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
