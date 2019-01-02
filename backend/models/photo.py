from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Device(Base):
    __tablename__ = "device"

    id = Column(Integer, primary_key=True)
    name = Column(String(250))


class Photo(Base):
    __tablename__ = "photo"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=True)
    filename = Column(String(250), nullable=False)

    device_id = Column(Integer, ForeignKey("device.id"))
    device = relationship(Device)


engine = create_engine("sqlite:///dev.db")
Base.metadata.create_all(engine)
