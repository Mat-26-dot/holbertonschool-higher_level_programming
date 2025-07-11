#!/usr/bin/python3

"""
A module that prints the State object with the name passed 
as argument from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":
    # To handle index error message
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <username> <password> <db_name> <state_name>")
        sys.exit (1)
    # Credentials to connect to database
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
    # Connect to database
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/{db_name}",
        pool_pre_ping=True
    )
    # Start a workspace for database operations
    Session = sessionmaker(bind=engine)
    session = Session()
    # Retrieve and sort records as python objects
    state = session.query(State).filter(
        State.name == state_name).first()
    # Display data in in format
    if state:
        for state in state_name:
            print(f"{state.id}: {state.name}")
    else:
        print("Not found")
    # Free resources and close database connection
    session.close()
