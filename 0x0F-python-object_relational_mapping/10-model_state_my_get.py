#!/usr/bin/python3
"""
This script lists all State objects
that contain letter 'a' from
the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Accesses the database and get the states
    from the database.
    """

    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)

    session = Session()

    instance = session.query(State).filter(State.name == argv[4]).first()
    if instance is None:
        print('Not found')
    else:
        print(instance.id)
