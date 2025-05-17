from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

from database.dbEngine import get_engine

Base = declarative_base()

class StopPlaces(Base):
    __tablename__ = 'stops'

    id = Column(String, primary_key=True)
    name = Column(String)
    lat = Column(Float)
    long = Column(Float)
    transportMode = Column(String)

    def __repr__(self):
        return f"Sted: {self.name}, id: {self.id}"


class Operators(Base):
    __tablename__ = 'operators'

    id = Column(String, primary_key=True)
    name = Column(String)
    url = Column(String)

    def __repr__(self):
        return f"Operatør: {self.name}, id: {self.id}"

