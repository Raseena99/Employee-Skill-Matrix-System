from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from .database import Base
class Employee(Base):
__tablename__ = "employees"
id = Column(Integer, primary_key=True, index=True)
name = Column(String, nullable=False)
email = Column(String, unique=True)
department = Column(String)
designation = Column(String)
experience = Column(Float)
skills = Column(String)
class User(Base):
__tablename__ = "users"
id = Column(Integer, primary_key=True, index=True)
username = Column(String, unique=True)
hashed_password = Column(String)
