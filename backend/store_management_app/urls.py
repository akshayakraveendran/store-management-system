from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, InventoryViewSet, ShippingViewSet, PurchaseViewSet,PurchaseItemViewSet,ItemTypeViewSet

router = DefaultRouter()
router.register('items', ItemViewSet)
router.register('item-types', ItemTypeViewSet)
router.register('inventory', InventoryViewSet)
router.register('shipping', ShippingViewSet)
router.register('purchases', PurchaseViewSet)
router.register('purchased-items', PurchaseItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]