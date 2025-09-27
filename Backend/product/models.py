from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://appuser:apppassword@postgres-db:5432/appdb"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Product(Base): 
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
