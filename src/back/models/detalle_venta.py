from sqlalchemy import Column, Integer, Text
from db import Base

class DetalleVenta(Base):
    __tablename__ = 'pos_detalle_venta'

    id = Column(Integer, primary_key=True, index=True)
    idVenta = Column(Integer, nullable=True)
    idProducto = Column(Integer, nullable=True)
    cantidad = Column(Integer, nullable=True)
    descripcion = Column(Text, nullable=True)
