#!/usr/bin/python3

"""
Module that prints the first State object from the database
hbtn_0e_6_usa
"""

from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <username> <password> <database>")
        sys.exit(1)
    
        # Parse command-line args    
        username=sys.argv[1],
        password=sys.argv[2],
        db_name=sys.argv[3]
    
    # Makes connection with db to communicate with db using SQLAlchemy
    # mysql+mysqldb - connect mysqldb with mysql driver
    engine = create_engine(
    f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
    pool_pre_ping=True
    )
    # Why this section is needed - lets you interact with db using python 
    # objects, not using raw SQL
    Session = sessionmaker(bind=engine)
    session = Session()

    # This query will retrieve the first state in the db in 
    # the order of State.id = .first(id)
    first_state = session.query(State).order_by(State.id).first()

    # Display the result 
    if first_state:
        print(f"{first_state.id}:{first_state.name}")
    else:
        print("Nothing")

    Session.close()




