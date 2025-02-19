from rest_framework import viewsets
from .models import Arma, Categoria
from .serializers import ArmaSerializer, CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet): 
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ArmaViewSet(viewsets.ModelViewSet):  
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer
