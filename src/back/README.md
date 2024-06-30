# SIGETRA Backend - 202410

SIGETRA backend es una API desarrollada con FastAPI que se conecta a una base de datos MySQL y proporciona operaciones CRUD básicas.

## Requisitos

- Python 3.7 o superior
- MySQL

## Instalación

### 1. Clonar el repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/juvega/proyecto-202410.git
cd proyecto-202410/src/back
```

### 2. Crear y activar un entorno virtual

Es una buena práctica usar un entorno virtual para aislar las dependencias del proyecto. Puedes crear y activar un entorno virtual con los siguientes comandos:

#### En Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### En macOS y Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

Con el entorno virtual activado, instala las dependencias requeridas utilizando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Configurar la base de datos

Asegúrate de tener una base de datos MySQL en funcionamiento. Crea la base de datos `pos_system` y configura el archivo `database.py` con tus credenciales de acceso a MySQL.

```python
# database.py
SQLALCHEMY_DATABASE_URL = "mysql://usuario:contraseña@localhost/pos_system"
```

### 5. Ejecutar las migraciones

Crea las tablas en la base de datos ejecutando el siguiente comando:

```bash
python -c 'from database import Base, engine; Base.metadata.create_all(bind=engine)'
```

### 6. Iniciar el servidor

Inicia el servidor FastAPI con el siguiente comando:

```bash
uvicorn main:app --reload
```

El servidor estará disponible en `http://127.0.0.1:8000`.

## Uso

Puedes acceder a la documentación interactiva de la API visitando `http://127.0.0.1:8000/docs`.

## Estructura del Proyecto

```
# Estructura de Carpetas del Proyecto

Este documento describe la estructura de carpetas utilizada en este proyecto. La organización de las carpetas está diseñada para mejorar la claridad y la eficiencia del desarrollo.

root/
│
├── main.py
├── db.py
├── create_tables.py
├── models/
│   ├── __init__.py
│   ├── caja.py
│   ├── categoria.py
│   ├── cliente.py
│   ├── detalle_venta.py
│   ├── producto.py
│   ├── serie.py
│   ├── tipo_afectacion.py
│   ├── tipo_comprobante.py
│   ├── tipo_documento.py
│   ├── usuario.py
│   ├── venta.py
├── crud/
│   ├── __init__.py
│   ├── caja.py
│   ├── categoria.py
│   ├── cliente.py
│   ├── detalle_venta.py
│   ├── producto.py
│   ├── serie.py
│   ├── tipo_afectacion.py
│   ├── tipo_comprobante.py
│   ├── tipo_documento.py
│   ├── usuario.py
│   ├── venta.py
├── schemas/
│   ├── __init__.py
│   ├── caja.py
│   ├── categoria.py
│   ├── cliente.py
│   ├── detalle_venta.py
│   ├── producto.py
│   ├── serie.py
│   ├── tipo_afectacion.py
│   ├── tipo_comprobante.py
│   ├── tipo_documento.py
│   ├── usuario.py
│   ├── venta.py
├── routers/
    ├── __init__.py
    ├── caja.py
    ├── categoria.py
    ├── cliente.py
    ├── detalle_venta.py
    ├── producto.py
    ├── serie.py
    ├── tipo_afectacion.py
    ├── tipo_comprobante.py
    ├── tipo_documento.py
    ├── usuario.py
    ├── venta.py
```


## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una rama con tu nueva funcionalidad: `git checkout -b nueva-funcionalidad`.
3. Realiza tus cambios y haz commit de ellos: `git commit -m 'Agregar nueva funcionalidad'`.
4. Sube tus cambios a tu repositorio fork: `git push origin nueva-funcionalidad`.
5. Abre un Pull Request en este repositorio.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
