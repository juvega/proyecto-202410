-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-06-2024 a las 03:24:19
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `data_micro`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pos_caja`
--

CREATE TABLE `pos_caja` (
  `id` int(11) NOT NULL,
  `nombre` text DEFAULT NULL,
  `asignacion` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pos_categorias`
--

CREATE TABLE `pos_categorias` (
  `id` int(11) NOT NULL,
  `categoria` text DEFAULT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pos_clientes`
--

CREATE TABLE `pos_clientes` (
  `id` int(11) NOT NULL,
  `tipo_documento` char(3) DEFAULT NULL,
  `nro_documento` varchar(11) DEFAULT NULL,
  `nombre_razonSocial` text DEFAULT NULL,
  `direccion` text DEFAULT NULL,
  `correo` text DEFAULT NULL,
  `celular` date DEFAULT NULL,
  `fecha_compra` int(11) DEFAULT NULL,
  `monto` float DEFAULT NULL,
  `fechaRegistro` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pos_detalle_venta`
--

CREATE TABLE `pos_detalle_venta` (
  `id` int(11) NOT NULL,
  `idVenta` int(11) DEFAULT NULL,
  `idProducto` int(11) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `descripcion` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pos_productos`
--

CREATE TABLE `pos_productos` (
  `id` int(11) NOT NULL,
  `imagen` text DEFAULT NULL,
  `codigo` varchar(50) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `categoria` int(11) DEFAULT NULL,
  `stock_min` int(11) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL,
  `precio_compra` float DEFAULT NULL,
  `precio_venta` float DEFAULT NULL,
  `tipo_precio` int(11) DEFAULT NULL,
  `tipo_afectacion` varchar(50) DEFAULT NULL,
  `ventas` int(11) DEFAULT NULL,
  `unidades` varchar(50) DEFAULT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pos_serie`
--

CREATE TABLE `pos_serie` (
  `id` int(11) NOT NULL,
  `caja` int(11) DEFAULT NULL,
  `tipo_comprobante` char(1) DEFAULT NULL,
  `correlativo` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pos_tipo_afectacion`
--

CREATE TABLE `pos_tipo_afectacion` (
  `codigo` char(2) NOT NULL,
  `descripcion` varchar(50) DEFAULT NULL,
  `nombre_afectacion` char(1) DEFAULT NULL,
  `tipo_afectacion` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pos_tipo_comprobante`
--

CREATE TABLE `pos_tipo_comprobante` (
  `codigo` char(1) NOT NULL,
  `descripcion` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pos_tipo_documento`
--

CREATE TABLE `pos_tipo_documento` (
  `codigo` char(3) NOT NULL,
  `descripcion` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pos_usuarios`
--

CREATE TABLE `pos_usuarios` (
  `id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` text DEFAULT NULL,
  `nombres` text DEFAULT NULL,
  `apellidos` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `admin_login` tinyint(1) DEFAULT NULL,
  `fecha` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pos_venta`
--

CREATE TABLE `pos_venta` (
  `id` int(11) NOT NULL,
  `serie` int(11) DEFAULT NULL,
  `fecha` date DEFAULT NULL,
  `fecha_hora` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `fecha_de_pago` date DEFAULT NULL,
  `estado` char(1) DEFAULT NULL,
  `tipo_comprobante` char(1) DEFAULT NULL,
  `igv_gravadas` float DEFAULT NULL,
  `igv_exoneradas` float DEFAULT NULL,
  `igv_inafectas` float DEFAULT NULL,
  `metodo_pago` text DEFAULT NULL,
  `cliente` int(11) DEFAULT NULL,
  `vendedor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `pos_caja`
--
ALTER TABLE `pos_caja`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pos_categorias`
--
ALTER TABLE `pos_categorias`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pos_clientes`
--
ALTER TABLE `pos_clientes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tipo_documento` (`tipo_documento`);

--
-- Indices de la tabla `pos_detalle_venta`
--
ALTER TABLE `pos_detalle_venta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idVenta` (`idVenta`),
  ADD KEY `idProducto` (`idProducto`);

--
-- Indices de la tabla `pos_productos`
--
ALTER TABLE `pos_productos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `categoria` (`categoria`),
  ADD KEY `tipo_afectacion` (`tipo_afectacion`);

--
-- Indices de la tabla `pos_serie`
--
ALTER TABLE `pos_serie`
  ADD PRIMARY KEY (`id`),
  ADD KEY `caja` (`caja`),
  ADD KEY `tipo_comprobante` (`tipo_comprobante`);

--
-- Indices de la tabla `pos_tipo_afectacion`
--
ALTER TABLE `pos_tipo_afectacion`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `pos_tipo_comprobante`
--
ALTER TABLE `pos_tipo_comprobante`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `pos_tipo_documento`
--
ALTER TABLE `pos_tipo_documento`
  ADD PRIMARY KEY (`codigo`);

--
-- Indices de la tabla `pos_usuarios`
--
ALTER TABLE `pos_usuarios`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pos_venta`
--
ALTER TABLE `pos_venta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `serie` (`serie`),
  ADD KEY `tipo_comprobante` (`tipo_comprobante`),
  ADD KEY `cliente` (`cliente`),
  ADD KEY `vendedor` (`vendedor`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `pos_caja`
--
ALTER TABLE `pos_caja`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pos_categorias`
--
ALTER TABLE `pos_categorias`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pos_clientes`
--
ALTER TABLE `pos_clientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pos_detalle_venta`
--
ALTER TABLE `pos_detalle_venta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pos_productos`
--
ALTER TABLE `pos_productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pos_serie`
--
ALTER TABLE `pos_serie`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pos_usuarios`
--
ALTER TABLE `pos_usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `pos_venta`
--
ALTER TABLE `pos_venta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `pos_clientes`
--
ALTER TABLE `pos_clientes`
  ADD CONSTRAINT `pos_clientes_ibfk_1` FOREIGN KEY (`tipo_documento`) REFERENCES `pos_tipo_documento` (`codigo`);

--
-- Filtros para la tabla `pos_detalle_venta`
--
ALTER TABLE `pos_detalle_venta`
  ADD CONSTRAINT `pos_detalle_venta_ibfk_1` FOREIGN KEY (`idVenta`) REFERENCES `pos_venta` (`id`),
  ADD CONSTRAINT `pos_detalle_venta_ibfk_2` FOREIGN KEY (`idProducto`) REFERENCES `pos_productos` (`id`);

--
-- Filtros para la tabla `pos_productos`
--
ALTER TABLE `pos_productos`
  ADD CONSTRAINT `pos_productos_ibfk_1` FOREIGN KEY (`categoria`) REFERENCES `pos_categorias` (`id`),
  ADD CONSTRAINT `pos_productos_ibfk_2` FOREIGN KEY (`tipo_afectacion`) REFERENCES `pos_tipo_afectacion` (`codigo`);

--
-- Filtros para la tabla `pos_serie`
--
ALTER TABLE `pos_serie`
  ADD CONSTRAINT `pos_serie_ibfk_1` FOREIGN KEY (`caja`) REFERENCES `pos_caja` (`id`),
  ADD CONSTRAINT `pos_serie_ibfk_2` FOREIGN KEY (`tipo_comprobante`) REFERENCES `pos_tipo_comprobante` (`codigo`);

--
-- Filtros para la tabla `pos_venta`
--
ALTER TABLE `pos_venta`
  ADD CONSTRAINT `pos_venta_ibfk_1` FOREIGN KEY (`serie`) REFERENCES `pos_serie` (`id`),
  ADD CONSTRAINT `pos_venta_ibfk_2` FOREIGN KEY (`tipo_comprobante`) REFERENCES `pos_tipo_comprobante` (`codigo`),
  ADD CONSTRAINT `pos_venta_ibfk_3` FOREIGN KEY (`cliente`) REFERENCES `pos_clientes` (`id`),
  ADD CONSTRAINT `pos_venta_ibfk_4` FOREIGN KEY (`vendedor`) REFERENCES `pos_usuarios` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
