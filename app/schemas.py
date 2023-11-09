from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint



class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Userout(BaseModel):
    id: int 
    username: str
    created_at: datetime
    Level: str
    class cofig:
        orm_mode = True

class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    owner_id: int
    owner: Userout  #this line uses the owner line in the models.py under post function

    class cofig:
        orm_mode = True

# class UserCreate(BaseModel):
#     email: EmailStr
#     password: str

class UserCreate(BaseModel):
    username: str
    password: str
    Level: str = 'Admin' 



class UserLogin(BaseModel):
    username: str
    password: str
    


class Token(BaseModel):
    access_token: str
    token_type: str
    Level: str
    

class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)


class PostWithVoteCount(BaseModel):
    id: int
    title: str
    content: str
    vote_count: int
