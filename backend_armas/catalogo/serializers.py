from rest_framework import serializers
from .models import Arma, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ArmaSerializer(serializers.ModelSerializer):
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())  # 👈 Esto usará solo el ID de la categoría

    class Meta:
        model = Arma
        fields = '__all__'
