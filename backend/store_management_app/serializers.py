from rest_framework import serializers
from .models import Item,ItemType,Inventory, Purchase,PurchasedItem,Shipping

class ItemTypeSerializer(serializers.ModelSerializer):
   class Meta:
      model=ItemType
      fields= '__all__'

class ItemSerializer(serializers.ModelSerializer):
   class Meta:
      model=Item
      fields='__all__'

class InventorySerializer(serializers.ModelSerializer):
   class Meta:
      model=Inventory
      fields='__all__'

class ShippingSerializer(serializers.ModelSerializer):
   class Meta:
      model=Shipping
      fields='__all__'

class PurchaseSerializer(serializers.ModelSerializer):
   class Meta:
      model=Purchase
      fields='__all__'

class PurchasedItemSerializer(serializers.ModelSerializer):
   class Meta:
      model=PurchasedItem
      fields='__all__'
