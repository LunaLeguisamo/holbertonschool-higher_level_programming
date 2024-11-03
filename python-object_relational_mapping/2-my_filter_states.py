#!/usr/bin/python3
"""
This module connects to a MySQL database and
retrieves states matching a given name.
"""


import sys
import MySQLdb


def main():
    """
    Main function to fetch and display states matching the name.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, database=database)

    sql_query = (
        "SELECT * FROM states WHERE name = {%s} ORDER BY id ASC"
        ).format(name)
    
    cursor = db.cursor()
    cursor.execute(sql_query)

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
