#!/usr/bin/python3
"""
module
"""
import sys
import MySQLdb
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    module
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         password=password, database=database)

    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all
    for state in states:
        print("{}: {}".format(state.id, state))


if __name__ == "__main__":
    main()
