#!/usr/bin/python3
"""Module connects to database using MySQLdb client using values passed
through command line arguments by using parameters to protect from a
sql injection attack"""
import sys
import MySQLdb

if __name__ == "__main__":
    host = 'localhost'
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                   (state,))
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
