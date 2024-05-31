from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import crud_service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/persons/', response_model=schemas.ReadPersonsSchema)
def create_persons(persons: schemas.CreatePersonsSchema, db: Session = Depends(get_db)):
    return crud_service.create_persons(db=db, persons=persons)

@router.get('/persons/', response_model=List[schemas.ReadPersonsSchema])
def read_personss(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_service.get_persons(db=db, skip=skip, limit=limit)

@router.get('/persons/{id}', response_model=schemas.ReadPersonsSchema)
def read_persons(id: int, db: Session = Depends(get_db)):
    db_persons = crud_service.get_persons_by_id(db=db, id=id)
    if db_persons is None:
        raise HTTPException(status_code=404, detail='Item not found')
    return db_persons

@router.put('/persons/{id}', response_model=schemas.ReadPersonsSchema)
def update_persons(id: int, persons: schemas.CreatePersonsSchema, db: Session = Depends(get_db)):
    db_persons = crud_service.update_persons(db=db, id=id, persons=persons)
    if db_persons is None:
        raise HTTPException(status_code=404, detail='Item not found')
    return db_persons

@router.delete('/persons/{id}')
def delete_persons(id: int, db: Session = Depends(get_db)):
    db_persons = crud_service.delete_persons(db=db, id=id)
    if db_persons is None:
        raise HTTPException(status_code=404, detail='Item not found')
    return db_persons

