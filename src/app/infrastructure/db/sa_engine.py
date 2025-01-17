from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, registry

from src.settings import Settings

metadata = MetaData()
mapper_registry = registry(metadata=metadata)
engine = create_engine(Settings.DATABASE_URL, echo=Settings.DEBUG)
Base = declarative_base(metadata=metadata)
SessionLocal = sessionmaker(bind=engine)
