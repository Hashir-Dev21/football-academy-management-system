from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import DeclarativeBase, relationship

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

    team_id = Column(Integer, ForeignKey("teams.id"), nullable=True)

    academy = relationship("Academy", back_populates="players")

    team = relationship("Team", back_populates="players")

    fees = relationship("Fee", back_populates="player")

    attendance = relationship(
    "Attendance",
    back_populates="player"
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    role = Column(String, nullable=False, default="Player")

    academy_id = Column(Integer, ForeignKey("academies.id"))

    academy = relationship("Academy")


class Fee(Base):
    __tablename__ = "fees"

    id = Column(Integer, primary_key=True, index=True)

    player_id = Column(Integer, ForeignKey("players.id"))

    month = Column(String, nullable=False)

    amount = Column(Float, nullable=False)

    due_date = Column(String, nullable=False)

    status = Column(String, default="Unpaid")

    voucher_no = Column(String, unique=True, nullable=False)

    player = relationship("Player", back_populates="fees")  


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)

    player_id = Column(Integer, ForeignKey("players.id"))

    date = Column(String, nullable=False)

    status = Column(String, nullable=False)

    player = relationship(
        "Player",
        back_populates="attendance"
    )

class Coach(Base):
    __tablename__ = "coaches"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String, nullable=False)

    age = Column(Integer)

    specialization = Column(String)

    experience = Column(Integer)

    phone = Column(String)
    
    academy_id = Column(Integer, ForeignKey("academies.id"))

    academy = relationship("Academy")

class Training(Base):
    __tablename__ = "trainings"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    training_date = Column(Date, nullable=False)

    training_time = Column(String, nullable=False)

    location = Column(String)

    coach_id = Column(Integer, ForeignKey("coaches.id"))


    coach = relationship("Coach")

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)

    team_name = Column(String, nullable=False)

    age_group = Column(String)
    
    academy_id = Column(Integer, ForeignKey("academies.id"))

    academy = relationship("Academy")

    players = relationship("Player", back_populates="team")

class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)

    home_team_id = Column(Integer, ForeignKey("teams.id"))
    away_team_id = Column(Integer, ForeignKey("teams.id"))

    match_date = Column(String)
    match_time = Column(String)
    venue = Column(String)

    home_score = Column(Integer, default=0)
    away_score = Column(Integer, default=0)

    status = Column(String, default="Scheduled")

    home_team = relationship(
        "Team",
        foreign_keys=[home_team_id]
    )

    away_team = relationship(
        "Team",
        foreign_keys=[away_team_id]
    )