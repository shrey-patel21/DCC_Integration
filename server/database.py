from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite Database URL
DATABASE_URL = "sqlite:///./inventory.db"

# Create engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Define Inventory Table
class InventoryItem(Base):
    __tablename__ = "inventory"

    name = Column(String, primary_key=True, index=True)
    quantity = Column(Integer, default=0)

# Create database tables
def init_db():
    Base.metadata.create_all(bind=engine)
