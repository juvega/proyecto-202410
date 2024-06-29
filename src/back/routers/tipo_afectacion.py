from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from db import get_db

router = APIRouter()

@router.get("/tipos_afectacion/", response_model=List[schemas.TipoAfectacion])
def read_tipos_afectacion(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tipos_afectacion = crud.get_tipos_afectacion(db, skip=skip, limit=limit)
    return tipos_afectacion

@router.post("/tipos_afectacion/", response_model=schemas.TipoAfectacion)
def create_tipo_afectacion(tipo_afectacion: schemas.TipoAfectacionCreate, db: Session = Depends(get_db)):
    return crud.create_tipo_afectacion(db=db, tipo_afectacion=tipo_afectacion)

@router.put("/tipos_afectacion/{tipo_afectacion_codigo}", response_model=schemas.TipoAfectacion)
def update_tipo_afectacion(tipo_afectacion_codigo: str, tipo_afectacion: schemas.TipoAfectacionUpdate, db: Session = Depends(get_db)):
    db_tipo_afectacion = crud.get_tipo_afectacion(db, tipo_afectacion_codigo=tipo_afectacion_codigo)
    if db_tipo_afectacion is None:
        raise HTTPException(status_code=404, detail="TipoAfectacion not found")
    return crud.update_tipo_afectacion(db=db, tipo_afectacion_codigo=tipo_afectacion_codigo, tipo_afectacion=tipo_afectacion)

@router.delete("/tipos_afectacion/{tipo_afectacion_codigo}", response_model=schemas.TipoAfectacion)
def delete_tipo_afectacion(tipo_afectacion_codigo: str, db: Session = Depends(get_db)):
    db_tipo_afectacion = crud.get_tipo_afectacion(db, tipo_afectacion_codigo=tipo_afectacion_codigo)
    if db_tipo_afectacion is None:
        raise HTTPException(status_code=404, detail="TipoAfectacion not found")
    return crud.delete_tipo_afectacion(db=db, tipo_afectacion_codigo=tipo_afectacion_codigo)
