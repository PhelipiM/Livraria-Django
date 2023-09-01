from rest_framework.serializers import ModelSerializer

from livraria.models import Compra

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="usuario.email", read_only=True)