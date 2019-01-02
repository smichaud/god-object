from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.photo import Base, Device, Photo

engine = create_engine("sqlite:///dev.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()
