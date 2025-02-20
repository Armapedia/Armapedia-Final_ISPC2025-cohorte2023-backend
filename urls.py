from django.urls import path
from .views import ArmaListCreateView, CategoriaListCreateView

urlpatterns = [
    path('categorias/', CategoriaListCreateView.as_view(), name='lista_categorias'),
    path('armas/', ArmaListCreateView.as_view(), name='lista_armas'),
]
