#Archivo creado por mi
from django.urls import path, include
from .views import home_view, CrearPublicacion, ListarPublicaciones, ListarEnDetalle, EliminarPublicacion, ActualizarPublicacion

urlpatterns = [
    path('',home_view, name="home"),
    path('crear_publicacion', CrearPublicacion.as_view(), name="crear_publicacion"),
    path('listar_publicaciones', ListarPublicaciones.as_view(), name="listar_publicaciones"),
    path('publicacion_en_detalle/<int:pk>', ListarEnDetalle.as_view(), name="publicacion_en_detalle"),
    path('confirmar_eliminar/<int:pk>', EliminarPublicacion.as_view(), name="confirmar_eliminar"),
    path('actualizar_publicacion/<int:pk>', ActualizarPublicacion.as_view(), name="actualizar_publicacion"),
]