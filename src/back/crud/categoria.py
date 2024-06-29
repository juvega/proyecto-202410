from sqlalchemy.orm import Session
from models.categoria import Categoria
from schemas.categoria import CategoriaCreate, CategoriaUpdate

def get_categoria(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()

def get_categorias(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Categoria).offset(skip).limit(limit).all()

def create_categoria(db: Session, categoria: CategoriaCreate):
    db_categoria = Categoria(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def update_categoria(db: Session, categoria_id: int, categoria: CategoriaUpdate):
    db_categoria = get_categoria(db, categoria_id)
    if db_categoria:
        for key, value in categoria.dict(exclude_unset=True).items():
            setattr(db_categoria, key, value)
        db.commit()
        db.refresh(db_categoria)
    return db_categoria

def delete_categoria(db: Session, categoria_id: int):
    db_categoria = get_categoria(db, categoria_id)
    if db_categoria:
        db.delete(db_categoria)
        db.commit()
    return db_categoria
