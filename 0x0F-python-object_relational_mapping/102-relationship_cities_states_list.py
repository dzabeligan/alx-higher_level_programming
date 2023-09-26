#!/usr/bin/python3
"""Lists all City objects from the database hbtn_0e_101_usa.
Usage: ./102-relationship_cities_states_list.py <mysql username> /
                                                <mysql password> /
                                                <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
       @localhost/{sys.argv[3]}",
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for city in session.query(City).order_by(City.id):
        print(f"{city.id}: {city.name} -> {city.state.name}")
