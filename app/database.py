from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


DATABASE_URI = settings.DATABASE_URI

if not DATABASE_URI:
    raise ValueError("DATABASE_URI not found")

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
