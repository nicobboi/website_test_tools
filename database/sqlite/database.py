from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database location (in this case is LOCAL)
SQLALCHEMY_DATABASE_URL = "sqlite:///app.db"

# create an engine for the local database and a new local session
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class for db models
Base = declarative_base()