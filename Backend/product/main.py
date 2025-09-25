from fastapi import FastAPI
from sqlalchemy.orm import Session
from models import Base, engine, Product

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/products")
def get_products():
    session = Session(bind=engine)
    products = session.query(Product).all()
    session.close()
    return [{"id": u.id, "name": u.name} for u in products]

@app.post("/products")
def create_product(name: str):
    session = Session(bind=engine)
    product = Product(name=name)
    session.add(product)
    session.commit()
    session.close()
    return {"message": "Product created"}
