#!/usr/bin/python3

"""
This module lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    
    conn = MySQLdb.connect( 
        host='localhost',
        user='root',
        passwd='my_native_password',
        db='db_name',
        port=3306
)


cursor = conn.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
