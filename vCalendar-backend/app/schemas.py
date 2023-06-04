from datetime import datetime

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
