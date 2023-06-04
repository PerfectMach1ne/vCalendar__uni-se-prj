from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


# ****************************** User schemas
class UserLogin(BaseModel):
    email: EmailStr
    hashed_password: str


class UserCreate(BaseModel):
    email: EmailStr
    hashed_password: str
    name: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    name: str
    # calendar_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None