from django.db import models

# Create your models here.
#Customer Model
class Customer(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=20)

    def get_customer_initials(self):
        return self.firstname[0] + self.lastname[0]

    def __str__(self):
        return f'''CUSTOMER #{self.id}
NAME: {self.firstname} {self.lastname}
ADDRESS: {self.address}
CITY: {self.city}'''
    
#Food Model    
class Food(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_food_shortname(self):
        return self.name[0:3]

    def __str__(self):
        return f'''FOOD # {self.pk} 
NAME: {self.name}
DESCRIPTION: {self.description}
PRICE: {self.price}'''
    
#Order Model
class Order (models.Model):
    PAYMENT_MODE_CHOICES = [
        ('CH', 'Cash'),
        ('CD', 'Card'),
        ('DW', 'Digital Wallet'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    orderdatetime = models.DateTimeField(auto_now_add=True, null=True) #used to get current date time, disables the editing features in the future
    paymentmode = models.CharField(max_length=2, choices=PAYMENT_MODE_CHOICES, null=True) #CH, CD, DW

    def total_order_price(self):
        total=0
        for customerorder in self.customerorder_set.all():
            total+=customerorder.total_price()
        return total

    def __str__(self):
        return f'''ORDER #{self.id}
CUSTOMER NAME: {self.customer.firstname} {self.customer.lastname}
PAYMENT MODE: {self.paymentmode}
ORDER DATE AND TIME: {self.orderdatetime}
'''
    
#Customer Model 
class CustomerOrder (models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def total_price(self):
        return self.quantity * self.food.price    

    def __str__(self):
        return f''' FOOD NAME: {self.food.name}
FOOD QUANTITY: {self.quantity}'''
    