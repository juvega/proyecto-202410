from sqlalchemy.orm import Session
from models.tipo_documento import TipoDocumento
from schemas.tipo_documento import TipoDocumentoCreate, TipoDocumentoUpdate

def get_tipo_documento(db: Session, tipo_documento_codigo: str):
    return db.query(TipoDocumento).filter(TipoDocumento.codigo == tipo_documento_codigo).first()

def get_tipos_documento(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TipoDocumento).offset(skip).limit(limit).all()

def create_tipo_documento(db: Session, tipo_documento: TipoDocumentoCreate):
    db_tipo_documento = TipoDocumento(**tipo_documento.dict())
    db.add(db_tipo_documento)
    db.commit()
    db.refresh(db_tipo_documento)
    return db_tipo_documento

def update_tipo_documento(db: Session, tipo_documento_codigo: str, tipo_documento: TipoDocumentoUpdate):
    db_tipo_documento = get_tipo_documento(db, tipo_documento_codigo)
    if db_tipo_documento:
        for key, value in tipo_documento.dict(exclude_unset=True).items():
            setattr(db_tipo_documento, key, value)
        db.commit()
        db.refresh(db_tipo_documento)
    return db_tipo_documento

def delete_tipo_documento(db: Session, tipo_documento_codigo: str):
    db_tipo_documento = get_tipo_documento(db, tipo_documento_codigo)
    if db_tipo_documento:
        db.delete(db_tipo_documento)
        db.commit()
    return db_tipo_documento
