from fastapi import FastAPI
from sqlalchemy.orm import Session
from models import Base, engine, User

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/users")
def get_users():
    session = Session(bind=engine)
    users = session.query(User).all()
    session.close()
    return [{"id": u.id, "name": u.name} for u in users]

@app.post("/users")
def create_user(name: str):
    session = Session(bind=engine)
    user = User(name=name)
    session.add(user)
    session.commit()
    session.close()
    return {"message": "User created"}
