from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from db import get_db

router = APIRouter()

@router.get("/tipos_comprobante/", response_model=List[schemas.TipoComprobante])
def read_tipos_comprobante(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tipos_comprobante = crud.get_tipos_comprobante(db, skip=skip, limit=limit)
    return tipos_comprobante

@router.post("/tipos_comprobante/", response_model=schemas.TipoComprobante)
def create_tipo_comprobante(tipo_comprobante: schemas.TipoComprobanteCreate, db: Session = Depends(get_db)):
    return crud.create_tipo_comprobante(db=db, tipo_comprobante=tipo_comprobante)

@router.put("/tipos_comprobante/{tipo_comprobante_codigo}", response_model=schemas.TipoComprobante)
def update_tipo_comprobante(tipo_comprobante_codigo: str, tipo_comprobante: schemas.TipoComprobanteUpdate, db: Session = Depends(get_db)):
    db_tipo_comprobante = crud.get_tipo_comprobante(db, tipo_comprobante_codigo=tipo_comprobante_codigo)
    if db_tipo_comprobante is None:
        raise HTTPException(status_code=404, detail="TipoComprobante not found")
    return crud.update_tipo_comprobante(db=db, tipo_comprobante_codigo=tipo_comprobante_codigo, tipo_comprobante=tipo_comprobante)

@router.delete("/tipos_comprobante/{tipo_comprobante_codigo}", response_model=schemas.TipoComprobante)
def delete_tipo_comprobante(tipo_comprobante_codigo: str, db: Session = Depends(get_db)):
    db_tipo_comprobante = crud.get_tipo_comprobante(db, tipo_comprobante_codigo=tipo_comprobante_codigo)
    if db_tipo_comprobante is None:
        raise HTTPException(status_code=404, detail="TipoComprobante not found")
    return crud.delete_tipo_comprobante(db=db, tipo_comprobante_codigo=tipo_comprobante_codigo)
