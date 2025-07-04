#!/usr/bin/python3

"""
This module takes an argument and displays all values in the states table
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Initialise Args #
    cities = sys.argv[4]
    # Connect to the MySQL database #
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        cities=sys.argv[4]
    )
    # Create a cursor and execute the query #
    cursor = conn.cursor()
    query = ("SELECT * FROM states WHERE BINARY name = '{}' "
             "ORDER BY cities.id ASC")
    # Query is parsed separately to the database to prevent name tampering
    # such as SQL injection #
    cursor.execute(query, (cities,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
        
