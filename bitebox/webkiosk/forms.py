from django.forms import ModelForm
from .models import Customer, Food, Order, CustomerOrder

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'description', 'price']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'paymentmode']

class CustomerOrderForm(ModelForm):
    class Meta:
        model = CustomerOrder
        fields = ['food', 'quantity' ]

class AddCustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'address', 'city']
    
#class CustomerDetailOrder(ModelForm):
    #class Meta:
        #model= Customer, Order, CustomerOrder, Food
        #fields = ['firstname', 'lastname', 'food', 'quantity', 'price', 'ordernumber', 'orderdateandtime']