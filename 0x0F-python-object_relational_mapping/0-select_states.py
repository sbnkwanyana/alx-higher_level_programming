#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    host = 'localhost'
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    data = cursor.fetchall()
    for row in data:
        print(f"({row[0]}, {row[1]})")
    cursor.close()
    db.close()
