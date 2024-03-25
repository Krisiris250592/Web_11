from datetime import datetime, date
from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    birt_day: date

    class Config:
        orm_mode = True


class ContactResponse(ContactModel):
    id: int

    class Config:
        orm_mode = True
