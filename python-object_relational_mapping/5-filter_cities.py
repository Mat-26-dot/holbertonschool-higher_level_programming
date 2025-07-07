#!/usr/bin/python3

"""
This module takes an argument and displays all values in the states table
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              "<state.id>"
              .format(sys.argv[0]))
        sys.exit(1)

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
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    # Query is parsed separately to the database to prevent name tampering
    # such as SQL injection #
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    conn.close()
