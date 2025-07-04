#!/usr/bin/python3

"""
This module takes an argument and displays all values in the states table
"""

import MySQLdb
import sys

if __name__ == "__main__":
    state_name = sys.argv[4]
    # Connect to the MySQL database #
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    # Create a cursor and execute the query #
    cursor = conn.cursor()
    query = ("SELECT * FROM states WHERE BINARY name = '%s' "
                   "ORDER BY states.id ASC")
    cursor.execute(query, state_name,)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
