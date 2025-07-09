#!/usr/bin/python3
 
"""
lists all State objects from the database hbtn_0e_6_usa
"""


from model_state import Base, State
import MySQLdb
import sys
import sqlalchemy

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    user, password, db_name, state_name = sys.argv[1:5]
    
    state_name=sys.argv[4]
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
)
    cursor = conn.cursor()
    query = ("SELECT * FROM State WHERE BINARY name = '%s' "
             "ORDER BY states.id ASC")

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
