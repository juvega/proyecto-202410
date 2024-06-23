CREATE DATABASE sigetra_db;
GO

USE sigetra_db;
GO

CREATE TABLE data_micro_pos_tipo_comprobante (
    codigo CHAR(1) NOT NULL PRIMARY KEY,
    descripcion VARCHAR(100)
);

CREATE TABLE data_micro_pos_tipo_documento (
    codigo CHAR(3) NOT NULL PRIMARY KEY,
    descripcion VARCHAR(50)
);

CREATE TABLE data_micro_pos_tipo_afectacion (
    codigo CHAR(2) NOT NULL PRIMARY KEY,
    descripcion VARCHAR(50),
    nombre_afectacion CHAR(1),
    tipo_afectacion CHAR(1)
);

CREATE TABLE data_micro_pos_categorias (
    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    categoria TEXT,
    fecha DATETIME
);

CREATE TABLE data_micro_pos_usuarios (
    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    username VARCHAR(50),
    password TEXT,
    nombres TEXT,
    apellidos TEXT,
    admin_login BIT,
    fecha DATETIME
);

CREATE TABLE data_micro_pos_productos (
    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    imagen TEXT,
    codigo VARCHAR(50),
    descripcion TEXT,
    categoria INT,
    stock_min INT,
    stock INT,
    precio_compra FLOAT,
    precio_venta FLOAT,
    tipo_precio INT,
    tipo_afectacion VARCHAR(50),
    ventas INT,
    unidades VARCHAR(50),
    fecha DATETIME,
    FOREIGN KEY (categoria) REFERENCES data_micro_pos_categorias(id),
    FOREIGN KEY (tipo_afectacion) REFERENCES data_micro_pos_tipo_afectacion(codigo)
);

CREATE TABLE data_micro_pos_serie (
    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    caja INT,
    tipo_comprobante CHAR(1),
    correlativo INT,
    FOREIGN KEY (tipo_comprobante) REFERENCES data_micro_pos_tipo_comprobante(codigo)
);

CREATE TABLE data_micro_pos_caja (
    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    nombre TEXT,
    asignacion INT
);

CREATE TABLE data_micro_pos_clientes (
    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    tipo_documento CHAR(3),
    nro_documento VARCHAR(11),
    nombre_razonSocial TEXT,
    direccion TEXT,
    correo TEXT,
    celular DATE,
    fecha_compra DATE,
    monto FLOAT,
    fechaRegistro DATETIME,
    FOREIGN KEY (tipo_documento) REFERENCES data_micro_pos_tipo_documento(codigo)
);

CREATE TABLE data_micro_pos_venta (
    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    serie INT,
    fecha DATE,
    fecha_hora DATETIME,
    fecha_de_pago DATE,
    estado CHAR(1),
    tipo_comprobante CHAR(1),
    igv_gravadas FLOAT,
    igv_exoneradas FLOAT,
    igv_inafectas FLOAT,
    metodo_pago TEXT,
    cliente INT,
    vendedor INT,
    FOREIGN KEY (tipo_comprobante) REFERENCES data_micro_pos_tipo_comprobante(codigo),
    FOREIGN KEY (cliente) REFERENCES data_micro_pos_clientes(id),
    FOREIGN KEY (vendedor) REFERENCES data_micro_pos_usuarios(id)
);

CREATE TABLE data_micro_pos_detalle_venta (
    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    idVenta INT,
    idProducto INT,
    cantidad INT,
    descripcion TEXT,
    FOREIGN KEY (idVenta) REFERENCES data_micro_pos_venta(id),
    FOREIGN KEY (idProducto) REFERENCES data_micro_pos_productos(id)
);
