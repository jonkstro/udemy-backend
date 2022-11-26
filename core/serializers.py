from rest_framework import serializers
from .models import List, Item


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'done']


class ListSerializer(serializers.HyperlinkedModelSerializer):
    # ADICIONAR ITEM_SET, POIS ITEM ESTÁ DENTRO DE UMA LISTA, ASSIM TEREMOS
    # ITENS EM CASCATA NO BANCO DE DADOS. MANY=TRUE => VÁRIOS ITEMS POR LISTA
    item_set = ItemSerializer(many=True)
    class Meta:
        model = List
        fields = ['id', 'name', 'owner', 'url', 'item_set']
