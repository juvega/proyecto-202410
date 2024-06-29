from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from db import get_db

router = APIRouter()

@router.get("/detalles_venta/", response_model=List[schemas.DetalleVenta])
def read_detalles_venta(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    detalles_venta = crud.get_detalles_venta(db, skip=skip, limit=limit)
    return detalles_venta

@router.post("/detalles_venta/", response_model=schemas.DetalleVenta)
def create_detalle_venta(detalle_venta: schemas.DetalleVentaCreate, db: Session = Depends(get_db)):
    return crud.create_detalle_venta(db=db, detalle_venta=detalle_venta)

@router.put("/detalles_venta/{detalle_venta_id}", response_model=schemas.DetalleVenta)
def update_detalle_venta(detalle_venta_id: int, detalle_venta: schemas.DetalleVentaUpdate, db: Session = Depends(get_db)):
    db_detalle_venta = crud.get_detalle_venta(db, detalle_venta_id=detalle_venta_id)
    if db_detalle_venta is None:
        raise HTTPException(status_code=404, detail="DetalleVenta not found")
    return crud.update_detalle_venta(db=db, detalle_venta_id=detalle_venta_id, detalle_venta=detalle_venta)

@router.delete("/detalles_venta/{detalle_venta_id}", response_model=schemas.DetalleVenta)
def delete_detalle_venta(detalle_venta_id: int, db: Session = Depends(get_db)):
    db_detalle_venta = crud.get_detalle_venta(db, detalle_venta_id=detalle_venta_id)
    if db_detalle_venta is None:
        raise HTTPException(status_code=404, detail="DetalleVenta not found")
    return crud.delete_detalle_venta(db=db, detalle_venta_id=detalle_venta_id)
