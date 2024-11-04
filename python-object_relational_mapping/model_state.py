#!/usr/bin/python3
"""
Module to define a State class and create a MySQL table.
This script connects to a MySQL database and creates a table
to store states using SQLAlchemy.
"""


import sys
import MySQLdb
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Define the State class to map to the 'states' table in the database."""
    __tablename__ = 'states'
    id = Column(
        Integer,
        autoincrement=1,
        unique=True,
        primary_key=True,
        insert_default=1
        )
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, database=database)

    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)
