from sqlalchemy.orm import Session
from models.tipo_comprobante import TipoComprobante
from schemas.tipo_comprobante import TipoComprobanteCreate, TipoComprobanteUpdate

def get_tipo_comprobante(db: Session, tipo_comprobante_codigo: str):
    return db.query(TipoComprobante).filter(TipoComprobante.codigo == tipo_comprobante_codigo).first()

def get_tipos_comprobante(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TipoComprobante).offset(skip).limit(limit).all()

def create_tipo_comprobante(db: Session, tipo_comprobante: TipoComprobanteCreate):
    db_tipo_comprobante = TipoComprobante(**tipo_comprobante.dict())
    db.add(db_tipo_comprobante)
    db.commit()
    db.refresh(db_tipo_comprobante)
    return db_tipo_comprobante

def update_tipo_comprobante(db: Session, tipo_comprobante_codigo: str, tipo_comprobante: TipoComprobanteUpdate):
    db_tipo_comprobante = get_tipo_comprobante(db, tipo_comprobante_codigo)
    if db_tipo_comprobante:
        for key, value in tipo_comprobante.dict(exclude_unset=True).items():
            setattr(db_tipo_comprobante, key, value)
        db.commit()
        db.refresh(db_tipo_comprobante)
    return db_tipo_comprobante

def delete_tipo_comprobante(db: Session, tipo_comprobante_codigo: str):
    db_tipo_comprobante = get_tipo_comprobante(db, tipo_comprobante_codigo)
    if db_tipo_comprobante:
        db.delete(db_tipo_comprobante)
        db.commit()
    return db_tipo_comprobante
