from django.urls import path
from .views import Index, CreateProduct, ReadProduct, UpdateProduct, DeleteProduct

urlpatterns = [
  path('', Index, name='index'),
  path('agregar/', CreateProduct, name='agregar'),
  path('productos/', ReadProduct, name='productos'),
  path('editar/<int:cod_product>/', UpdateProduct, name='editar'),
  path('eliminar/<int:cod_product>/', DeleteProduct, name='eliminar'),
]