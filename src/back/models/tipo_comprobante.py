from sqlalchemy import Column, String
from db import Base

class TipoComprobante(Base):
    __tablename__ = 'pos_tipo_comprobante'

    codigo = Column(String(1), primary_key=True, index=True)
    descripcion = Column(String(100), nullable=True)
