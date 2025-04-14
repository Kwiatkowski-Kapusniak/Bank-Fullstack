# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models.user import User
from app.crud.user_crud import create_user, get_user_by_username
from app.schemas.user_schema import UserCreate, UserInDB

# Utwórz tabele w bazie danych
User.metadata.create_all(bind=engine)

app = FastAPI()

# Funkcja do uzyskiwania sesji z bazy danych
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint do rejestracji użytkownika
@app.post("/register", response_model=UserInDB)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db=db, user=user)

# Endpoint do logowania użytkownika
@app.get("/user/{username}", response_model=UserInDB)
def get_user(username: str, db: Session = Depends(get_db)):
    db_user = get_user_by_username(db, username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
