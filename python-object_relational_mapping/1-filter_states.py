#!/usr/bin/python3
"""
This module connects to a MySQL database and retrieves all states
with names starting with 'N'.
"""

import sys
import MySQLdb


def main():
    """
    Main function to fetch and display states starting with 'N'.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, password=password, db=database)

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE BINARY nameLIKE 'N%' ORDER BY id ASC"
        )

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
