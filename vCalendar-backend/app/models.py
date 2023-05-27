from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, text, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    calendar_id = Column(Integer, ForeignKey('calendars.id'))
    calendar = relationship("Calendar", back_populates="user")

    modified_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'),
                         onupdate=text('current_timestamp()'))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class Calendar(Base):
    __tablename__ = "calendars"
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="calendar")

    modified_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'),
                         onupdate=text('current_timestamp()'))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class EventGroup(Base):
    __tablename__ = "events"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    is_visible = Column(Boolean, index=True)

    event_array = Column(String, index=True)
    style = Column(String, index=True)

    owner_id = Column(Integer, ForeignKey("calendars.id"))
    calendar = relationship("Calendar")

    modified_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'),
                         onupdate=text('current_timestamp()'))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class Reminder(Base):
    __tablename__ = "reminders"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    is_done = Column(Boolean, index=True)

    is_visible = Column(Boolean, index=True)
    start_date = Column(DateTime, index=True)
    end_date = Column(DateTime, index=True)

    modified_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'),
                         onupdate=text('current_timestamp()'))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    style = Column(String, index=True)

    is_visible = Column(Boolean, index=True)
    start_date = Column(DateTime, index=True)
    end_date = Column(DateTime, index=True)

    modified_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'),
                         onupdate=text('current_timestamp()'))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
