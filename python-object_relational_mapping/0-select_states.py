#!/usr/bin/python3
import MySQLdb
import sys
"""
This module create a function that manipulate database with python
"""

def main():
    """Fetches and lists all states from the hbtn_0e_0_usa database.
    This script connects to a MySQL database and retrieves all entries
    from the 'states' table, ordered by the state ID. It expects three
    command line arguments: MySQL username, password, and database name.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, password=password, db=database)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
