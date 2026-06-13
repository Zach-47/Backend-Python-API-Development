from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Literal, Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class ConfigDict:
        from_attributes = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    #convert schemas to orm compatible format
    class ConfigDict:
        from_attributes = True

class PostOut(BaseModel):
    Post: Post
    votes: int
    class ConfigDict:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: Literal[0,1]