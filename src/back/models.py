from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, TIMESTAMP, Date
from sqlalchemy.orm import relationship
from database import Base

class TipoComprobante(Base):
    __tablename__ = 'data_micro_pos_tipo_comprobante'
    codigo = Column(String(1), primary_key=True, index=True)
    descripcion = Column(String(100))

class TipoDocumento(Base):
    __tablename__ = 'data_micro_pos_tipo_documento'
    codigo = Column(String(3), primary_key=True, index=True)
    descripcion = Column(String(50))

class TipoAfectacion(Base):
    __tablename__ = 'data_micro_pos_tipo_afectacion'
    codigo = Column(String(2), primary_key=True, index=True)
    descripcion = Column(String(50))
    nombre_afectacion = Column(String(1))
    tipo_afectacion = Column(String(1))

class Categoria(Base):
    __tablename__ = 'data_micro_pos_categorias'
    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(Text)
    fecha = Column(TIMESTAMP)

class Usuario(Base):
    __tablename__ = 'data_micro_pos_usuarios'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    password = Column(Text)
    nombres = Column(Text)
    apellidos = Column(Text)
    admin_login = Column(Integer)
    fecha = Column(TIMESTAMP)

class Producto(Base):
    __tablename__ = 'data_micro_pos_productos'
    id = Column(Integer, primary_key=True, index=True)
    imagen = Column(Text)
    codigo = Column(String(50))
    descripcion = Column(Text)
    categoria = Column(Integer, ForeignKey('data_micro_pos_categorias.id'))
    stock_min = Column(Integer)
    stock = Column(Integer)
    precio_compra = Column(Float)
    precio_venta = Column(Float)
    tipo_precio = Column(Integer)
    tipo_afectacion = Column(String(50), ForeignKey('data_micro_pos_tipo_afectacion.codigo'))
    ventas = Column(Integer)
    unidades = Column(String(50))
    fecha = Column(TIMESTAMP)

class Serie(Base):
    __tablename__ = 'data_micro_pos_serie'
    id = Column(Integer, primary_key=True, index=True)
    caja = Column(Integer)
    tipo_comprobante = Column(String(1), ForeignKey('data_micro_pos_tipo_comprobante.codigo'))
    correlativo = Column(Integer)

class Caja(Base):
    __tablename__ = 'data_micro_pos_caja'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(Text)
    asignacion = Column(Integer)

class Cliente(Base):
    __tablename__ = 'data_micro_pos_clientes'
    id = Column(Integer, primary_key=True, index=True)
    tipo_documento = Column(String(3), ForeignKey('data_micro_pos_tipo_documento.codigo'))
    nro_documento = Column(String(11))
    nombre_razonSocial = Column(Text)
    direccion = Column(Text)
    correo = Column(Text)
    celular = Column(Date)
    fecha_compra = Column(Date)
    monto = Column(Float)
    fechaRegistro = Column(TIMESTAMP)

class Venta(Base):
    __tablename__ = 'data_micro_pos_venta'
    id = Column(Integer, primary_key=True, index=True)
    serie = Column(Integer, ForeignKey('data_micro_pos_serie.id'))
    fecha = Column(Date)
    fecha_hora = Column(TIMESTAMP)
    fecha_de_pago = Column(Date)
    estado = Column(String(1))
    tipo_comprobante = Column(String(1), ForeignKey('data_micro_pos_tipo_comprobante.codigo'))
    igv_gravadas = Column(Float)
    igv_exoneradas = Column(Float)
    igv_inafectas = Column(Float)
    metodo_pago = Column(Text)
    cliente = Column(Integer, ForeignKey('data_micro_pos_clientes.id'))
    vendedor = Column(Integer, ForeignKey('data_micro_pos_usuarios.id'))

class DetalleVenta(Base):
    __tablename__ = 'data_micro_pos_detalle_venta'
    id = Column(Integer, primary_key=True, index=True)
    idVenta = Column(Integer, ForeignKey('data_micro_pos_venta.id'))
    idProducto = Column(Integer, ForeignKey('data_micro_pos_productos.id'))
    cantidad = Column(Integer)
    descripcion = Column(Text)
