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
    state = sys.argv[4]
    db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name "
                   "FROM cities LEFT JOIN states "
                   "ON cities.state_id = states.id "
                   "WHERE states.name = %s ORDER BY "
                   "cities.id ASC", (state,))
    data = cursor.fetchall()
    print(", ".join([row[0] for row in data]))
    cursor.close()
    db.close()
