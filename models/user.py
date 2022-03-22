from typing import Optional
from pydantic import BaseModel, EmailStr, validator, constr

class User(BaseModel):
    id: Optional[str] = None
    email: EmailStr
    name: str
    surname: str
    gender: str
    description: str
    hashed_password: str

class UserSend(BaseModel):
    email: EmailStr
    name: str
    surname: str
    gender: str
    description: str
    password: constr(min_length=8)
    confirm_pass: str

    @validator("confirm_pass")
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values["password"]:
            raise ValueError("password hasn`t matched")
        return v
