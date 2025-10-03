from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import Base, engine, Order

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/orders")
def get_orders():
    session = Session(bind=engine)
    orders = session.query(Order).all()
    session.close()
    return [{"id": o.id, "user_id": o.user_id, "product_id": o.product_id, "quantity": o.quantity} for o in orders]

@app.post("/orders")
def create_order(
    user_id: int = Query(...),
    product_id: int = Query(...),
    quantity: int = Query(...)
):
    session = Session(bind=engine)
    order = Order(user_id=user_id, product_id=product_id, quantity=quantity)
    session.add(order)
    session.commit()
    session.close()
    return {"message": "Order created"}

