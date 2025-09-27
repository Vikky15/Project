from fastapi import FastAPI
from sqlalchemy.orm import Session
from models import Base, engine, Order

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/orders")
def get_orders():
    session = Session(bind=engine)
    orders = session.query(Order).all()
    session.close()
    return [{"id": u.id, "name": u.name} for u in orders]

@app.post("/orders")
def create_order(name: str):
    session = Session(bind=engine)
    order = Order(name=name)
    session.add(order)
    session.commit()
    session.close()
    return {"message": "Order created"}
