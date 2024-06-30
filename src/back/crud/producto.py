from sqlalchemy.orm import Session
from models.producto import Producto
from schemas.producto import ProductoCreate, ProductoUpdate
from datetime import datetime

def get_producto(db: Session, producto_id: int):
    return db.query(Producto).filter(Producto.id == producto_id).first()

def get_productos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Producto).offset(skip).limit(limit).all()

def create_producto(db: Session, producto: ProductoCreate):
    db_producto = Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def update_producto(db: Session, producto_id: int, producto: ProductoUpdate):
    db_producto = get_producto(db, producto_id)
    if db_producto:
        db_producto.fecha = datetime.utcnow()
        for key, value in producto.dict(exclude_unset=True).items():
            setattr(db_producto, key, value)
        db.commit()
        db.refresh(db_producto)
    return db_producto

def delete_producto(db: Session, producto_id: int):
    db_producto = get_producto(db, producto_id)
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto
