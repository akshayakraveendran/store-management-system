from django.db import models

# Create your models here.
class ItemType(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


class Item(models.Model):

    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    item_type=models.ForeignKey(ItemType, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Inventory(models.Model):

    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    description=models.CharField(max_length=255)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Shipping(models.Model):

    recipient_name=models.CharField(max_length=50)
    address=models.CharField(max_length=255)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    pin=models.CharField(max_length=10)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Purchase(models.Model):

    total_price=models.DecimalField(max_digits=10, decimal_places=2)
    discount_amount=models.DecimalField(max_digits=10, decimal_places=2)
    tax_amount=models.DecimalField(max_digits=10, decimal_places=2)
    sub_total=models.DecimalField(max_digits=10, decimal_places=2)
    shipping=models.ForeignKey(Shipping, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class PurchasedItem(models.Model):

    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    purchase=models.ForeignKey(Purchase, on_delete=models.CASCADE)
    quantity=models.DecimalField(max_digits=10, decimal_places=2)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

