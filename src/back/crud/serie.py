from sqlalchemy.orm import Session
from models.serie import Serie
from schemas.serie import SerieCreate, SerieUpdate

def get_serie(db: Session, serie_id: int):
    return db.query(Serie).filter(Serie.id == serie_id).first()

def get_series(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Serie).offset(skip).limit(limit).all()

def create_serie(db: Session, serie: SerieCreate):
    db_serie = Serie(**serie.dict())
    db.add(db_serie)
    db.commit()
    db.refresh(db_serie)
    return db_serie

def update_serie(db: Session, serie_id: int, serie: SerieUpdate):
    db_serie = get_serie(db, serie_id)
    if db_serie:
        for key, value in serie.dict(exclude_unset=True).items():
            setattr(db_serie, key, value)
        db.commit()
        db.refresh(db_serie)
    return db_serie

def delete_serie(db: Session, serie_id: int):
    db_serie = get_serie(db, serie_id)
    if db_serie:
        db.delete(db_serie)
        db.commit()
    return db_serie
