from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from db import get_db

router = APIRouter()

@router.get("/cajas/", response_model=List[schemas.Caja])
def read_cajas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    cajas = crud.get_cajas(db, skip=skip, limit=limit)
    return cajas

@router.post("/cajas/", response_model=schemas.Caja)
def create_caja(caja: schemas.CajaCreate, db: Session = Depends(get_db)):
    return crud.create_caja(db=db, caja=caja)

@router.put("/cajas/{caja_id}", response_model=schemas.Caja)
def update_caja(caja_id: int, caja: schemas.CajaUpdate, db: Session = Depends(get_db)):
    db_caja = crud.get_caja(db, caja_id=caja_id)
    if db_caja is None:
        raise HTTPException(status_code=404, detail="Caja not found")
    return crud.update_caja(db=db, caja_id=caja_id, caja=caja)

@router.delete("/cajas/{caja_id}", response_model=schemas.Caja)
def delete_caja(caja_id: int, db: Session = Depends(get_db)):
    db_caja = crud.get_caja(db, caja_id=caja_id)
    if db_caja is None:
        raise HTTPException(status_code=404, detail="Caja not found")
    return crud.delete_caja(db=db, caja_id=caja_id)
