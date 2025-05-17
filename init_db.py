from database import Base, engine
from pipelines import load_stop_places_to_db, load_operators_to_db

def main():
    print("Creating tables...")
    Base.metadata.create_all(engine)
    print("Tables created.")

    print("Loading stop places...")
    load_stop_places_to_db()
    
    print("Loading operators...")
    load_operators_to_db()

    print("Done")

if __name__ == "__main__":
    main()