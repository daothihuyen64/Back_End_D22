from pydantic import BaseModel
from datetime import datetime


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    
class UserBase(BaseModel):
    email : str  
    user_name : str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True

class GroupBase(BaseModel):
    group_name : str
    description: str

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    created_date: datetime

    class Config:
        from_attributes = True

