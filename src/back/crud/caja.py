from sqlalchemy.orm import Session
from models.caja import Caja
from schemas.caja import CajaCreate, CajaUpdate

def get_caja(db: Session, caja_id: int):
    return db.query(Caja).filter(Caja.id == caja_id).first()

def get_cajas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Caja).offset(skip).limit(limit).all()

def create_caja(db: Session, caja: CajaCreate):
    db_caja = Caja(**caja.dict())
    db.add(db_caja)
    db.commit()
    db.refresh(db_caja)
    return db_caja

def update_caja(db: Session, caja_id: int, caja: CajaUpdate):
    db_caja = get_caja(db, caja_id)
    if db_caja:
        for key, value in caja.dict(exclude_unset=True).items():
            setattr(db_caja, key, value)
        db.commit()
        db.refresh(db_caja)
    return db_caja

def delete_caja(db: Session, caja_id: int):
    db_caja = get_caja(db, caja_id)
    if db_caja:
        db.delete(db_caja)
        db.commit()
    return db_caja
