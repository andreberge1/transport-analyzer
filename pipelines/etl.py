from sqlalchemy.orm import sessionmaker

from api import get_stopPlaces, get_operators
from database import StopPlaces, Operators, engine

def load_stop_places_to_db():
    data = get_stopPlaces()

    if not data:
        print("No data fetched from the API")
        return
    
    stop_places = [
        StopPlaces(
            id=stop['id'],
            name=stop['name'],
            lat=stop["latitude"],
            long=stop['longitude'],
            transportMode=stop['transportMode'][0] if stop['transportMode'] else 'unkown'
        )
        for stop in data['data']['stopPlaces']
    ]

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        session.query(StopPlaces).delete()
        session.add_all(stop_places)
        session.commit()
        print(f"Successfully loaded {len(stop_places)} stop places into the database.")
    except Exception as e:
        session.rollback()
        print(f"Error loading data into the database: {e}")
    finally:
        session.close()

def load_operators_to_db():
    data = get_operators()

    if not data:
        print("No data fetched from the API")
        return
    
    operators = [
        Operators(
            id=operator['id'],
            name=operator['name'],
            url=operator['url']
        )
        for operator in data['data']['operators']
    ]

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        session.query(Operators).delete()
        session.add_all(operators)
        session.commit()
        print(f"Succsessfully loaded {len(operators)} operators to the database.")
    except Exception as e:
        session.rollback()
        print(f"Error loading data into the database: {e}")
    finally:
        session.close()


