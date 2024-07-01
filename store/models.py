from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=255)


class Cart(models.Model):
    item = models.ForeignKey(Item, related_name="items")

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True)


class Order(models.Model):
    PENDING   = "P"
    COMPLETED = "C"
    FAILED    = "F"

    payment_choices = {
        PENDING:"pending",
        COMPLETED:"completed",
        FAILED: "failed"
    }


    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=payment_choices , default=PENDING)
    item = models.ForeignKey(Item , related_name="items")
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT related_name="orders")

class Collection(models.Model):
    title = models.CharField(max_length=255)
    
class Product(models.Model):
    title = models.CharField(max_length=65)
    description = models.TextField()
    price = models.DecimalField(max_digits=10 , decimal_places= 2)
    inventory = models.IntegerField()
    collection = models.ForeignKey(Collection, related_name='products')



    

