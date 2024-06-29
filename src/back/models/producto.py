from sqlalchemy import Column, Integer, Text, String, Float, TIMESTAMP
from db import Base

class Producto(Base):
    __tablename__ = 'pos_productos'

    id = Column(Integer, primary_key=True, index=True)
    imagen = Column(Text, nullable=True)
    codigo = Column(String(50), nullable=True)
    descripcion = Column(Text, nullable=True)
    categoria = Column(Integer, nullable=True)
    stock_min = Column(Integer, nullable=True)
    stock = Column(Integer, nullable=True)
    precio_compra = Column(Float, nullable=True)
    precio_venta = Column(Float, nullable=True)
    tipo_precio = Column(Integer, nullable=True)
    tipo_afectacion = Column(String(50), nullable=True)
    ventas = Column(Integer, nullable=True)
    unidades = Column(String(50), nullable=True)
    fecha = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
