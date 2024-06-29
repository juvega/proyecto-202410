from sqlalchemy.orm import Session
from models.detalle_venta import DetalleVenta
from schemas.detalle_venta import DetalleVentaCreate, DetalleVentaUpdate

def get_detalle_venta(db: Session, detalle_venta_id: int):
    return db.query(DetalleVenta).filter(DetalleVenta.id == detalle_venta_id).first()

def get_detalles_venta(db: Session, skip: int = 0, limit: int = 10):
    return db.query(DetalleVenta).offset(skip).limit(limit).all()

def create_detalle_venta(db: Session, detalle_venta: DetalleVentaCreate):
    db_detalle_venta = DetalleVenta(**detalle_venta.dict())
    db.add(db_detalle_venta)
    db.commit()
    db.refresh(db_detalle_venta)
    return db_detalle_venta

def update_detalle_venta(db: Session, detalle_venta_id: int, detalle_venta: DetalleVentaUpdate):
    db_detalle_venta = get_detalle_venta(db, detalle_venta_id)
    if db_detalle_venta:
        for key, value in detalle_venta.dict(exclude_unset=True).items():
            setattr(db_detalle_venta, key, value)
        db.commit()
        db.refresh(db_detalle_venta)
    return db_detalle_venta

def delete_detalle_venta(db: Session, detalle_venta_id: int):
    db_detalle_venta = get_detalle_venta(db, detalle_venta_id)
    if db_detalle_venta:
        db.delete(db_detalle_venta)
        db.commit()
    return db_detalle_venta
