from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, registry

from src.settings import config

metadata = MetaData()
mapper_registry = registry(metadata=metadata)
engine = create_engine(config.DATABASE_URL, echo=config.DEBUG)
Base = declarative_base(metadata=metadata)
SessionLocal = sessionmaker(bind=engine)
