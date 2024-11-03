#!/usr/bin/python3
"""
This module create a function that manipulate database with python
"""

import sys
import MySQLdb


def main():
    """
    Module
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, password=password, db=database)

    cursor = db.cursor
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        if state.name[0] == 'N':
            print(state)

    cursor.close()
    db.close()

    if __name__ == "__main__":
        main()
