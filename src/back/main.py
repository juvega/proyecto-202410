from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/categorias/", response_model=schemas.Categoria)
def create_categoria(categoria: schemas.Categoria, db: Session = Depends(get_db)):
    return crud.create_categoria(db=db, categoria=categoria)

@app.get("/categorias/", response_model=list[schemas.Categoria])
def read_categorias(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    categorias = crud.get_categorias(db, skip=skip, limit=limit)
    return categorias

@app.get("/categorias/{categoria_id}", response_model=schemas.Categoria)
def read_categoria(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria = crud.get_categoria(db, categoria_id=categoria_id)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria not found")
    return db_categoria

# Puedes agregar más rutas según sea necesario
