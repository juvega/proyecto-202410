from sqlalchemy.orm import Session
from models.venta import Venta
from schemas.venta import VentaCreate, VentaUpdate

def get_venta(db: Session, venta_id: int):
    return db.query(Venta).filter(Venta.id == venta_id).first()

def get_ventas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Venta).offset(skip).limit(limit).all()

def create_venta(db: Session, venta: VentaCreate):
    db_venta = Venta(**venta.dict())
    db.add(db_venta)
    db.commit()
    db.refresh(db_venta)
    return db_venta

def update_venta(db: Session, venta_id: int, venta: VentaUpdate):
    db_venta = get_venta(db, venta_id)
    if db_venta:
        for key, value in venta.dict(exclude_unset=True).items():
            setattr(db_venta, key, value)
        db.commit()
        db.refresh(db_venta)
    return db_venta

def delete_venta(db: Session, venta_id: int):
    db_venta = get_venta(db, venta_id)
    if db_venta:
        db.delete(db_venta)
        db.commit()
    return db_venta
