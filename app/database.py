from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"

# SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{DB_PASSWORD}@{DATABASE_HOST}/{DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
# Get a session to out db every time we have a request to access
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()