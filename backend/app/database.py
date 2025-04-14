# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:mojehaslo123@localhost:5432/bankapp"

engine = create_engine(DATABASE_URL)

# Tworzymy instancję Base (czyli bazę do mapowania tabel w SQLAlchemy)
Base = declarative_base()

# Tworzymy sesję
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
