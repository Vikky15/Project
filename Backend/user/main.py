from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import Base, engine, User

# Initialize FastAPI app
app = FastAPI()

# Enable CORS (important for frontend -> backend communication)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# GET all users
@app.get("/users")
def get_users():
    session = Session(bind=engine)
    users = session.query(User).all()
    session.close()
    return [{"id": u.id, "name": u.name} for u in users]

# POST create a new user
@app.post("/users")
def create_user(name: str):
    session = Session(bind=engine)
    user = User(name=name)
    session.add(user)
    session.commit()
    session.close()
    return {"message": "User created"}

