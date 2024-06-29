from sqlalchemy import Column, Integer, String, Text, Date, Float, TIMESTAMP
from db import Base

class Cliente(Base):
    __tablename__ = 'pos_clientes'

    id = Column(Integer, primary_key=True, index=True)
    tipo_documento = Column(String(3), nullable=True)
    nro_documento = Column(String(11), nullable=True)
    nombre_razonSocial = Column(Text, nullable=True)
    direccion = Column(Text, nullable=True)
    correo = Column(Text, nullable=True)
    celular = Column(Date, nullable=True)
    fecha_compra = Column(Integer, nullable=True)
    monto = Column(Float, nullable=True)
    fechaRegistro = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
