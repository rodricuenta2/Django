from django.urls import path
from . import views

# 2. punto de entrada aca se manejan todas las rutas (urls) de esta aplicacion
urlpatterns = [
path('', views.index, name='inicio_productos'),
]