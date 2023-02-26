from sqlalchemy import Column, String, Integer, Boolean

from database import Base


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    complate = Column(Boolean, default=False)
