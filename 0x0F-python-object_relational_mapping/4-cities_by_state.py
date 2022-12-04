#!/usr/bin/python3
"""
Module selects all cities by their states joined on state id
"""
import sys
import MySQLdb

if __name__ == "__main__":
    host = 'localhost'
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities LEFT JOIN states "
                   "ON cities.state_id = states.id ORDER BY "
                   "cities.id ASC")
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()
