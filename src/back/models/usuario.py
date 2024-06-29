from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from db import Base

class Usuario(Base):
    __tablename__ = 'pos_usuarios'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=True)
    password = Column(Text, nullable=True)
    nombres = Column(Text, nullable=True)
    apellidos = Column(Text, nullable=True)
    email = Column(Text, nullable=True)
    admin_login = Column(Integer, nullable=True)
    fecha = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
