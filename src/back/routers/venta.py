from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from db import get_db

router = APIRouter()

@router.get("/ventas/", response_model=List[schemas.Venta])
def read_ventas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    ventas = crud.get_ventas(db, skip=skip, limit=limit)
    return ventas

@router.post("/ventas/", response_model=schemas.Venta)
def create_venta(venta: schemas.VentaCreate, db: Session = Depends(get_db)):
    return crud.create_venta(db=db, venta=venta)

@router.put("/ventas/{venta_id}", response_model=schemas.Venta)
def update_venta(venta_id: int, venta: schemas.VentaUpdate, db: Session = Depends(get_db)):
    db_venta = crud.get_venta(db, venta_id=venta_id)
    if db_venta is None:
        raise HTTPException(status_code=404, detail="Venta not found")
    return crud.update_venta(db=db, venta_id=venta_id, venta=venta)

@router.delete("/ventas/{venta_id}", response_model=schemas.Venta)
def delete_venta(venta_id: int, db: Session = Depends(get_db)):
    db_venta = crud.get_venta(db, venta_id=venta_id)
    if db_venta is None:
        raise HTTPException(status_code=404, detail="Venta not found")
    return crud.delete_venta(db=db, venta_id=venta_id)
