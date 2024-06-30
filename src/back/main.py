from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import caja_router, categoria_router, cliente_router, detalle_venta_router, producto_router, serie_router, tipo_afectacion_router, tipo_comprobante_router, tipo_documento_router, usuario_router, venta_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las solicitudes de cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

app.include_router(caja_router, prefix="/api/v1", tags=["caja"])
app.include_router(categoria_router, prefix="/api/v1", tags=["categoria"])
app.include_router(cliente_router, prefix="/api/v1", tags=["cliente"])
app.include_router(detalle_venta_router, prefix="/api/v1", tags=["detalle_venta"])
app.include_router(producto_router, prefix="/api/v1", tags=["producto"])
app.include_router(serie_router, prefix="/api/v1", tags=["serie"])
app.include_router(tipo_afectacion_router, prefix="/api/v1", tags=["tipo_afectacion"])
app.include_router(tipo_comprobante_router, prefix="/api/v1", tags=["tipo_comprobante"])
app.include_router(tipo_documento_router, prefix="/api/v1", tags=["tipo_documento"])
app.include_router(usuario_router, prefix="/api/v1", tags=["usuario"])
app.include_router(venta_router, prefix="/api/v1", tags=["venta"])
