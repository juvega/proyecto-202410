from sqlalchemy.orm import Session
from models.tipo_afectacion import TipoAfectacion
from schemas.tipo_afectacion import TipoAfectacionCreate, TipoAfectacionUpdate

def get_tipo_afectacion(db: Session, tipo_afectacion_codigo: str):
    return db.query(TipoAfectacion).filter(TipoAfectacion.codigo == tipo_afectacion_codigo).first()

def get_tipos_afectacion(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TipoAfectacion).offset(skip).limit(limit).all()

def create_tipo_afectacion(db: Session, tipo_afectacion: TipoAfectacionCreate):
    db_tipo_afectacion = TipoAfectacion(**tipo_afectacion.dict())
    db.add(db_tipo_afectacion)
    db.commit()
    db.refresh(db_tipo_afectacion)
    return db_tipo_afectacion

def update_tipo_afectacion(db: Session, tipo_afectacion_codigo: str, tipo_afectacion: TipoAfectacionUpdate):
    db_tipo_afectacion = get_tipo_afectacion(db, tipo_afectacion_codigo)
    if db_tipo_afectacion:
        for key, value in tipo_afectacion.dict(exclude_unset=True).items():
            setattr(db_tipo_afectacion, key, value)
        db.commit()
        db.refresh(db_tipo_afectacion)
    return db_tipo_afectacion

def delete_tipo_afectacion(db: Session, tipo_afectacion_codigo: str):
    db_tipo_afectacion = get_tipo_afectacion(db, tipo_afectacion_codigo)
    if db_tipo_afectacion:
        db.delete(db_tipo_afectacion)
        db.commit()
    return db_tipo_afectacion
