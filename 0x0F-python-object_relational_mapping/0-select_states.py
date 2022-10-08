#!/usr/bin/python3
"""
Script that list all states from the database hbtn_0e_0_usa:
"""
import sys
import MySQLdb

def connectToDB():
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("select * from states ORDER BY id ASC")
    rows = cur.fetchAll()
    for item in rows:
        print(item)

if __name__ == "__main__":
    connectToDB()