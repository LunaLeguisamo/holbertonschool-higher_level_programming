#!/usr/bin/python3
"""
module
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """
    module
    """
    engine = create_engine('sqlite://')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{}: {}".format(state.id, state.name))

    session.close()


if __name__ == "__main__":
    main()
