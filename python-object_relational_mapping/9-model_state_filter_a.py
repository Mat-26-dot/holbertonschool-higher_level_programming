#!/usr/bin/python3

"""
 A module that lists all State objects that contain the
 letter 'a' from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import MySQLdb

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    # Create engine to communicate with db using SQLAlchemy
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{db_name}',
    )
    # Session lets you interact with db using python objects not SQL
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query: Filter state objects that contain letter 'a'
    states = session.query(State).filter\
        (State.name.ilike('%a%')).order_by(State.id).all()
    # Print results
    if states:
        for state in states:
            print(f"{state.id}: {state.name}")

    # Close session to save resources
    session.close()
