
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


from dotenv import load_dotenv
import os

load_dotenv()

# Database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set.")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

# Factory for creating new SQLAlchemy sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)



# Dependency to provide a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




