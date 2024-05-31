from sqlalchemy.orm import Session
import models, schemas

def get_persons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Persons).offset(skip).limit(limit).all()

def get_persons_by_id(db: Session, id: int):
    return db.query(models.Persons).filter(models.Persons.id == id).first()

def create_persons(db: Session, persons: schemas.CreatePersonsSchema):
    db_persons = models.Persons(**persons.dict())
    db.add(db_persons)
    db.commit()
    db.refresh(db_persons)
    return db_persons

def update_persons(db: Session, id: int, persons: schemas.CreatePersonsSchema):
    db_persons = db.query(models.Persons).filter(models.Persons.id == id).first()
    if db_persons is None:
        return None
    for key, value in persons.dict().items():
        setattr(db_persons, key, value)
    db.commit()
    db.refresh(db_persons)
    return db_persons

def delete_persons(db: Session, id: int):
    db_persons = db.query(models.Persons).filter(models.Persons.id == id).first()
    if db_persons is None:
        return None
    db.delete(db_persons)
    db.commit()
    return db_persons

