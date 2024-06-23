CREATE DATABASE sigetra_db;
USE sigetra_db;

CREATE TABLE data_micro_pos_tipo_comprobante (
    codigo CHAR(1) NOT NULL,
    descripcion VARCHAR(100),
    PRIMARY KEY (codigo)
);

CREATE TABLE data_micro_pos_tipo_documento (
    codigo CHAR(3) NOT NULL,
    descripcion VARCHAR(50),
    PRIMARY KEY (codigo)
);

CREATE TABLE data_micro_pos_tipo_afectacion (
    codigo CHAR(2) NOT NULL,
    descripcion VARCHAR(50),
    nombre_afectacion CHAR(1),
    tipo_afectacion CHAR(1),
    PRIMARY KEY (codigo)
);

CREATE TABLE data_micro_pos_categorias (
    id INT(11) NOT NULL AUTO_INCREMENT,
    categoria TEXT,
    fecha TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE data_micro_pos_usuarios (
    id INT(11) NOT NULL AUTO_INCREMENT,
    username VARCHAR(50),
    password TEXT,
    nombres TEXT,
    apellidos TEXT,
    admin_login TINYINT(1),
    fecha TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE data_micro_pos_productos (
    id INT(11) NOT NULL AUTO_INCREMENT,
    imagen TEXT,
    codigo VARCHAR(50),
    descripcion TEXT,
    categoria INT(11),
    stock_min INT(11),
    stock INT(11),
    precio_compra FLOAT,
    precio_venta FLOAT,
    tipo_precio INT(11),
    tipo_afectacion VARCHAR(50),
    ventas INT(11),
    unidades VARCHAR(50),
    fecha TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (categoria) REFERENCES data_micro_pos_categorias(id),
    FOREIGN KEY (tipo_afectacion) REFERENCES data_micro_pos_tipo_afectacion(codigo)
);

CREATE TABLE data_micro_pos_serie (
    id INT(11) NOT NULL AUTO_INCREMENT,
    caja INT(11),
    tipo_comprobante CHAR(1),
    correlativo INT(11),
    PRIMARY KEY (id),
    FOREIGN KEY (tipo_comprobante) REFERENCES data_micro_pos_tipo_comprobante(codigo)
);

CREATE TABLE data_micro_pos_caja (
    id INT(11) NOT NULL AUTO_INCREMENT,
    nombre TEXT,
    asignacion INT(11),
    PRIMARY KEY (id)
);

CREATE TABLE data_micro_pos_clientes (
    id INT(11) NOT NULL AUTO_INCREMENT,
    tipo_documento CHAR(3),
    nro_documento VARCHAR(11),
    nombre_razonSocial TEXT,
    direccion TEXT,
    correo TEXT,
    celular DATE,
    fecha_compra DATE,
    monto FLOAT,
    fechaRegistro TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY (tipo_documento) REFERENCES data_micro_pos_tipo_documento(codigo)
);

CREATE TABLE data_micro_pos_venta (
    id INT(11) NOT NULL AUTO_INCREMENT,
    serie INT(11),
    fecha DATE,
    fecha_hora TIMESTAMP,
    fecha_de_pago DATE,
    estado CHAR(1),
    tipo_comprobante CHAR(1),
    igv_gravadas FLOAT,
    igv_exoneradas FLOAT,
    igv_inafectas FLOAT,
    metodo_pago TEXT,
    cliente INT(11),
    vendedor INT(11),
    PRIMARY KEY (id),
    FOREIGN KEY (tipo_comprobante) REFERENCES data_micro_pos_tipo_comprobante(codigo),
    FOREIGN KEY (cliente) REFERENCES data_micro_pos_clientes(id),
    FOREIGN KEY (vendedor) REFERENCES data_micro_pos_usuarios(id)
);

CREATE TABLE data_micro_pos_detalle_venta (
    id INT(11) NOT NULL AUTO_INCREMENT,
    idVenta INT(11),
    idProducto INT(11),
    cantidad INT(11),
    descripcion TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (idVenta) REFERENCES data_micro_pos_venta(id),
    FOREIGN KEY (idProducto) REFERENCES data_micro_pos_productos(id)
);
