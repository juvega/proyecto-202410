from sqlalchemy import Column, Integer, Text
from db import Base

class Caja(Base):
    __tablename__ = 'pos_caja'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(Text, nullable=True)
    asignacion = Column(Integer, nullable=True)