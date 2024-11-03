#!/usr/bin/python3
"""
Module
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
    name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, database=database)

    sql_query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cursor = db.cursor()
    cursor.execute(sql_query, name)
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
