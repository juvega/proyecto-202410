from sqlalchemy import Column, Integer, String, Text, Float, Date, TIMESTAMP
from db import Base

class Venta(Base):
    __tablename__ = 'pos_venta'

    id = Column(Integer, primary_key=True, index=True)
    serie = Column(Integer, nullable=True)
    fecha = Column(Date, nullable=True)
    fecha_hora = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
    fecha_de_pago = Column(Date, nullable=True)
    estado = Column(String(1), nullable=True)
    tipo_comprobante = Column(String(1), nullable=True)
    igv_gravadas = Column(Float, nullable=True)
    igv_exoneradas = Column(Float, nullable=True)
    igv_inafectas = Column(Float, nullable=True)
    metodo_pago = Column(Text, nullable=True)
    cliente = Column(Integer, nullable=True)
    vendedor = Column(Integer, nullable=True)
