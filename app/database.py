from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from .config import settings

DATABASE_URI = settings.DATABASE_URI

if not DATABASE_URI:
    raise ValueError("DATABASE_URI not found")

engine = create_engine(
    DATABASE_URI,
    pool_pre_ping=True,
    connect_args={"sslmode": "require"}, 
)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except OperationalError as e:
        print("Database connection lost. Attempting to reconnect...")
        db.rollback()  
        db.close() 
        raise e
    finally:
        db.close()
