from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from db import get_db

router = APIRouter()

@router.get("/tipos_documento/", response_model=List[schemas.TipoDocumento])
def read_tipos_documento(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    tipos_documento = crud.get_tipos_documento(db, skip=skip, limit=limit)
    return tipos_documento

@router.post("/tipos_documento/", response_model=schemas.TipoDocumento)
def create_tipo_documento(tipo_documento: schemas.TipoDocumentoCreate, db: Session = Depends(get_db)):
    return crud.create_tipo_documento(db=db, tipo_documento=tipo_documento)

@router.put("/tipos_documento/{tipo_documento_codigo}", response_model=schemas.TipoDocumento)
def update_tipo_documento(tipo_documento_codigo: str, tipo_documento: schemas.TipoDocumentoUpdate, db: Session = Depends(get_db)):
    db_tipo_documento = crud.get_tipo_documento(db, tipo_documento_codigo=tipo_documento_codigo)
    if db_tipo_documento is None:
        raise HTTPException(status_code=404, detail="TipoDocumento not found")
    return crud.update_tipo_documento(db=db, tipo_documento_codigo=tipo_documento_codigo, tipo_documento=tipo_documento)

@router.delete("/tipos_documento/{tipo_documento_codigo}", response_model=schemas.TipoDocumento)
def delete_tipo_documento(tipo_documento_codigo: str, db: Session = Depends(get_db)):
    db_tipo_documento = crud.get_tipo_documento(db, tipo_documento_codigo=tipo_documento_codigo)
    if db_tipo_documento is None:
        raise HTTPException(status_code=404, detail="TipoDocumento not found")
    return crud.delete_tipo_documento(db=db, tipo_documento_codigo=tipo_documento_codigo)
