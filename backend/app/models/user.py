# app/models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# Importuj Base z app/database.py, żeby mieć dostęp do instancji Base
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
