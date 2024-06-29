from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Definir la URL de la base de datos MySQL. Asegúrate de actualizar esto con tus credenciales.
DATABASE_URL = os.getenv('DATABASE_URL', 'mysql://root:Welcome123!@localhost/sigetra_db')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
