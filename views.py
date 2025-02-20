from rest_framework import generics
from .models import Arma, Categoria
from .serializers import ArmaSerializer, CategoriaSerializer

class CategoriaListCreateView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ArmaListCreateView(generics.ListCreateAPIView):
    queryset = Arma.objects.all()
    serializer_class = ArmaSerializer
