from rest_framework import serializers
from .models import Item,ItemType,Inventory, Purchase,PurchasedItem,Shipping

class ItemTypeSerializer(serializers.ModelSerializer):
   class Meta:
      model=ItemType
      field= '__all__'

class ItemSerializer(serializers.ModelSerializer):
   class Meta:
      model=Item
      field='__all__'

class InventorySerializer(serializers.ModelSerializer):
   class Meta:
      model=Inventory
      field='__all__'

class ShippingSerializer(serializers.ModelSerializer):
   class Meta:
      model=Shipping
      field='__all__'

class PurchaseSerializer(serializers.ModelSerializer):
   class Meta:
      model=Purchase
      field='__all__'

class PurchasedItemSerializer(serializers.ModelSerializer):
   class Meta:
      model=PurchasedItem
      field='__all__'
