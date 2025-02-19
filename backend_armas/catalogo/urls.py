from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArmaViewSet, CategoriaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'armas', ArmaViewSet, basename='arma')

urlpatterns = [
    path('', include(router.urls)),  # 
]
