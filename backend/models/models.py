from sqlalchemy import Boolean, Column, String, Integer
from ..config.database import Base


class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    active = Column(Boolean, default=True)
    
class UserAdm(Base):
    __tablename__ = "user_adm"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    active = Column(Boolean, default=True)
    permission = Column(Boolean, default=False)
    
    
class UserMapped(User):
    pass
    
class UserAdmMapped(UserAdm):
    pass
    
