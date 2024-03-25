from typing import List

from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel


async def get_contacts(skip: int, limit: int, db: Session):
    return db.query(Contact).offset(skip).limit(limit).all()


async def create_contact(body: ContactModel, db: Session):
    print(body.first_name)
    contact = Contact(first_name=body.first_name, last_name=body.last_name, email=body.email,
                      phone=body.phone, birt_day=body.birt_day)

    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def get_contact_by_id(contact_id: int, db: Session) -> Contact | None:
    return db.query(Contact).filter(Contact.id == contact_id).first()


#
#
# async def create_tag(body: TagModel, db: Session) -> Tag:
#     tag = Tag(name=body.name)
#     db.add(tag)
#     db.commit()
#     db.refresh(tag)
#     return tag
#
#
async def update_contact(contact_id: int, body: ContactModel, db: Session) -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone = body.phone
        contact.birt_day = body.birt_day
        db.commit()
    return contact


async def remove_contact(contact_id: int, db: Session)  -> Contact | None:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def get_contact_by_info(contact_info: str, db: Session):
    # try:
    t = db.query(Contact).filter(Contact.first_name == contact_info).first()
    print("*"*50)
    print(t)
    print("*" * 50)
    return t

    # except Exception:
    #     pass
    # try:
    #     return db.query(Contact).filter(Contact.last_name == contact_info).all()
    # except Exception:
    #     pass
    # try:
    #     return db.query(Contact).filter(Contact.email == contact_info).first()
    # except Exception:
    #     pass
