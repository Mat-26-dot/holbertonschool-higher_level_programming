#!/usr/bin/python3

"""
 A module that lists all State objects that contain the 
 letter 'a' from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

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
    Session = Session()
    # Query: Filter state objects that contain letter 'a'
    results = Session.query(State.id).filter(State.name.like("a%"))

    if results:
        print(f"{results.id}: {results.name}")
    else:
        print("Nothing")
    
    Session.close()





