from django.db import models
import uuid
from authentication.models import User

# Referensi kode:
# https://www.youtube.com/watch?v=Tqtsb9105T0&t=1884s

# Create your models here.

# Model untuk products
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    product_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True,editable=False) # ID Unique
    image = models.ImageField()
    category = models.CharField(max_length=20,default="product")
    description = models.CharField()

    def __str__(self):
        return self.name


# Model untuk order
class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True,editable=False) # ID Unique
    completed = models.BooleanField(default=False) # Status pembayaran

    def __str__(self): 
        return self.owner.username
    
    # Menghitung total keseluruhan belanja
    @property 
    def grandtotal(self):
        cartitems = self.cartitems_set.all()
        total = 0
        for item in cartitems:
            total += item.subtotal
        return total
    
    @property 
    def cartquantity(self):
        cartitems = self.cartitems_set.all()
        total = 0
        for item in cartitems:
            total += item.quantity
        return total

# Models untuk setiap item di carts
class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self): 
        return self.product.name

    # Untuk menghitung total
    @property 
    def subtotal(self):
        total = self.quantity * self.product.price
        return total

# Models untuk menampung alamat user
class DeliveryAdress(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    postal = models.CharField(max_length=50)


    