from sqlalchemy.orm import Session
import models, schemas

def get_categoria(db: Session, categoria_id: int):
    return db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

def get_categorias(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Categoria).offset(skip).limit(limit).all()

def create_categoria(db: Session, categoria: schemas.Categoria):
    db_categoria = models.Categoria(categoria=categoria.categoria, fecha=categoria.fecha)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria