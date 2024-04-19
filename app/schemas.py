# library to specify the schema a user needs to use for the API
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional

# each model specifies what the user is allowed to change in a post

class PostBase(BaseModel):
    # this class using pydantic will check if there is a title and if it is a string,
    # and the same for content
    # default value is True
    title: str
    content: str
    published: bool = True

# class CreatePost(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#
# class UpdatePost(BaseModel):
#     title: str
#     content: str
#     published: bool

class PostCreate(PostBase):
    pass

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    # this is needed for sqlachemy to identify the class as a dict
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    # this is needed for sqlachemy to identify the class as a dict
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

class Token(BaseModel):
    access_token : str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)