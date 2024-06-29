from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from db import get_db

router = APIRouter()

@router.get("/series/", response_model=List[schemas.Serie])
def read_series(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    series = crud.get_series(db, skip=skip, limit=limit)
    return series

@router.post("/series/", response_model=schemas.Serie)
def create_serie(serie: schemas.SerieCreate, db: Session = Depends(get_db)):
    return crud.create_serie(db=db, serie=serie)

@router.put("/series/{serie_id}", response_model=schemas.Serie)
def update_serie(serie_id: int, serie: schemas.SerieUpdate, db: Session = Depends(get_db)):
    db_serie = crud.get_serie(db, serie_id=serie_id)
    if db_serie is None:
        raise HTTPException(status_code=404, detail="Serie not found")
    return crud.update_serie(db=db, serie_id=serie_id, serie=serie)

@router.delete("/series/{serie_id}", response_model=schemas.Serie)
def delete_serie(serie_id: int, db: Session = Depends(get_db)):
    db_serie = crud.get_serie(db, serie_id=serie_id)
    if db_serie is None:
        raise HTTPException(status_code=404, detail="Serie not found")
    return crud.delete_serie(db=db, serie_id=serie_id)
