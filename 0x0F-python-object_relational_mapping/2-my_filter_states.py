#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    host = 'localhost'
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    query = f"SELECT * FROM states WHERE name='{sys.argv[4]}' ORDER BY id ASC"
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=database)
    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
