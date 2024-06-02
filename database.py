from sqlmodel import Session, create_engine, SQLModel
from contextlib import contextmanager
from api import NutritionInfo

# Create database engine
engine = create_engine("sqlite:///database1.db")  # Ensure the desired path

# Create tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Session context manager
@contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()