from sqlalchemy import Column, Integer, String, Boolean, DateTime, INTEGER, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Persons(Base):
    __tablename__ = 'persons'
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(255), primary_key=False)

