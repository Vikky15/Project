from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://appuser:apppassword@db:5432/appdb"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)

