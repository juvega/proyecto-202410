from sqlalchemy import Column, Integer, String
from db import Base

class Serie(Base):
    __tablename__ = 'pos_serie'

    id = Column(Integer, primary_key=True, index=True)
    caja = Column(Integer, nullable=True)
    tipo_comprobante = Column(String(1), nullable=True)
    correlativo = Column(Integer, nullable=True)
