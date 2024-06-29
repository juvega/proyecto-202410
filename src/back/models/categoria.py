from sqlalchemy import Column, Integer, Text, TIMESTAMP
from db import Base

class Categoria(Base):
    __tablename__ = 'pos_categorias'

    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(Text, nullable=True)
    fecha = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
