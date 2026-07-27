from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class Base(DeclarativeBase):
    pass


class Academy(Base):
    __tablename__ = "academies"

    id = Column(Integer, primary_key=True, index=True)
    academy_name = Column(String, nullable=False)
    city = Column(String, nullable=False)
    contact = Column(String, nullable=False)

    players = relationship("Player", back_populates="academy")


class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    position = Column(String, nullable=False)

    academy_id = Column(Integer, ForeignKey("academies.id"))

    academy = relationship("Academy", back_populates="players")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    role = Column(String, nullable=False, default="Player")

    academy_id = Column(Integer, ForeignKey("academies.id"))

    academy = relationship("Academy")