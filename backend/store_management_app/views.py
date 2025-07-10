from django.shortcuts import render
from rest_framework import viewsets
from .models import Item, ItemType,Inventory, Purchase,PurchasedItem,Shipping
from .serializers import ItemSerializer, ItemTypeSerializer,InventorySerializer, PurchaseSerializer,PurchasedItemSerializer,ShippingSerializer

class ItemTypeViewSet(viewsets.ModelViewSet):
    queryset=ItemType.objects.all()
    serializer_class=ItemTypeSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset=Item.objects.all()
    serializer_class=ItemSerializer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset=Inventory.objects.all()
    serializer_class=InventorySerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset=Purchase.objects.all()
    serializer_class=PurchaseSerializer

class PurchaseItemViewSet(viewsets.ModelViewSet):
    queryset=PurchasedItem.objects.all()
    serializer_class=PurchasedItemSerializer

class ShippingViewSet(viewsets.ModelViewSet):
    queryset=Shipping.objects.all()
    serializer_class=ShippingSerializer

