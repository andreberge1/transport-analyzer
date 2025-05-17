#https://medium.com/@ramanbazhanau/mastering-sqlalchemy-a-comprehensive-guide-for-python-developers-ddb3d9f2e829

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

username = os.getenv("USER")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")
db = os.getenv("DATABASE")

def get_engine():
    return create_engine(
        f"postgresql://{username}:{password}@localhost:{port}/{db}",
        echo=True)