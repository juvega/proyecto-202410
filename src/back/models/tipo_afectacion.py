from sqlalchemy import Column, String
from db import Base

class TipoAfectacion(Base):
    __tablename__ = 'pos_tipo_afectacion'

    codigo = Column(String(2), primary_key=True, index=True)
    descripcion = Column(String(50), nullable=True)
    nombre_afectacion = Column(String(1), nullable=True)
    tipo_afectacion = Column(String(1), nullable=True)
