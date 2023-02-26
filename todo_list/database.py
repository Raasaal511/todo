from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


CONNTECT_TO_DATABASE = str(dotenv_values('../.env')['CONNECT_TO_DATABASE'])

engine = create_engine(CONNTECT_TO_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
