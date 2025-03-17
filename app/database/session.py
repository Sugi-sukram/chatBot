from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

username = "postgres"
password = "Erdster%40123"
host = "localhost"
port = "5432"
database = "ArtificialIntelligence"

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"

# Create the PostgreSQL engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for models
Base = declarative_base()
