from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import Base, engine, Product

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

@app.get("/products")
def get_products():
    session = Session(bind=engine)
    products = session.query(Product).all()
    session.close()
    return [{"id": p.id, "name": p.name, "price": p.price} for p in products]

@app.post("/products")
def create_product(name: str, price: float):
    session = Session(bind=engine)
    product = Product(name=name, price=price)
    session.add(product)
    session.commit()
    session.close()
    return {"message": "Product created"}

