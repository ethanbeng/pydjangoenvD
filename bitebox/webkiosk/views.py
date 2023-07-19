from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.forms import inlineformset_factory, modelformset_factory
from .models import Food, Customer, Order, CustomerOrder
from .forms import FoodForm, OrderForm, CustomerOrderForm, AddCustomerForm#, CustomerDetailOrder
from django.contrib.auth import authenticate, login

# Create your views here.
def index (request):
    return render (request, 'webkiosk/welcome.html')

def testview (request):
    return render (request, 'webkiosk/testpage.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('webkiosk:index')  # Redirect to the home page after successful login
        else:
            error = 'Invalid credentials'
            return render(request, 'webkiosk/login.html', {'error': error})

    return render(request, 'webkiosk/login.html')

# ------------------ FOOD VIEWS ------------------

def listfood(request):
    fl = Food.objects.all()
    context = {'foodlist': fl}
    return render (request, 'webkiosk/food_list.html', context)

def createfood(request):
    if request.method == "GET":
        f = FoodForm()
    elif request.method == "POST":
        f= FoodForm(request.POST)
        # print(f)
        if f.is_valid():
            f.save()
            return redirect('webkiosk:food-list') #can also use '/webkiosk/menu/' in the parenthesis
            # print('saved')
        else:
            print('invalid form')

    context = {'form': f, 'formheading': 'Add Food'}
    return render (request, 'webkiosk/food_form.html', context)

def detailfood(request, pk):
    f = Food.objects.get(id=pk)
    context = {'food': f}
    return render(request, 'webkiosk/food_detail.html', context)

def updatefood(request, pk):    
    food = Food.objects.get(id=pk)
    if request.method == "GET":
        form = FoodForm(instance=food)
    elif request.method == 'POST':
        form = FoodForm(request.POST,instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food record successfully updated.')
        else:
            print('invalid form') 
    context = {'form': form,'formheading': 'Update Food'}
    return render(request, 'webkiosk/food_form.html', context)

def deletefood(request, pk):
    f = Food.objects.get(id=pk) # gets a food record based on the id
    # this object is an instance of the Food model
    if request.method == 'GET':
        context = {'food': f}
        return render(request, 'webkiosk/food_delete.html', context)
    elif request.method == 'POST':
        f.delete()
        return redirect('webkiosk:food-list')
    
# ------------------ ORDER VIEWS ------------------

def createorder(request):
    if request.method == "POST":
        of = OrderForm(request.POST)
        if of.is_valid():
            o = of.save()
            context = {'order' : o}
            return render(request, 'webkiosk/order_detail.html', context)
    else:
        of = OrderForm()
    context = {'OrderForm': of, 'formheading': 'Order Food'}
    return render(request, 'webkiosk/food_order.html', context)

def customerorder(request, pk):
    order=Order.objects.get(id=pk)
    if request.method == 'POST':
        #print('post request customer order form')
        COFormSet = inlineformset_factory (Order, CustomerOrder, form=CustomerOrderForm, extra=4, can_delete=True)
        formset = COFormSet(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
            #items = formset.save(commit=False)
            # set the order that they belong to before committing to the db
            #for item in items:
                #item.order = order
                #item.save()            
            #print(CustomerOrderForm.errors)
            orderitems = CustomerOrder.objects.filter(order=order)
            context = {'order': order, 'orderitems': orderitems}
            return render(request, 'webkiosk/order_detail.html', context)
    else:
        #print('should be an empty form')
        COFormSet = inlineformset_factory(Order, CustomerOrder, form=CustomerOrderForm, extra=4, can_delete=True)
        formset = COFormSet(instance=order)
    context = {'formset': formset}
    return render(request, 'webkiosk/customer_order.html', context)
        
def detailorder(request, pk):
    o = Order.objects.get(id=pk)
    print(o)
    # get all the order items in the order
    orderitems = CustomerOrder.objects.filter(order=o)
    print(orderitems)
    context = {'order': o, 'orderitems': orderitems}
    return render(request, 'webkiosk/order_detail.html', context)

def listorder(request):
    ol = Order.objects.all()
    print(ol)
    context = {'orderlist': ol}
    return render (request, 'webkiosk/order_list.html', context)

def updateorder(request, pk):    
    order = Order.objects.get(id=pk)
    customerorders = CustomerOrder.objects.filter(order=order)
    COFormSet = modelformset_factory (CustomerOrder, form=CustomerOrderForm, extra=4, can_delete=True)
    if request.method == 'POST':
        COFormSet = modelformset_factory (CustomerOrder, form=CustomerOrderForm, extra=4, can_delete=True)
        formset = COFormSet(request.POST, queryset = customerorders)
        if formset.is_valid():
            items = formset.save(commit=False)
            # set the order that they belong to before committing to the db
            for item in items:
                item.order = order
                item.save()       
            messages.success(request, 'Order record successfully updated.')
            orderitems = CustomerOrder.objects.filter(order=order)(instance=order)
        context = {'order': order, 'orderitems': orderitems, 'formheading': 'Update Order'}
        return render(request, 'webkiosk/order_detail.html', context)
    else:
        formset = COFormSet(request.POST, queryset = customerorders)
        context = {'order': order, 'formset': formset}   
        return render(request, 'webkiosk/order_list.html', context)
    
def deleteorder(request, pk):
    o = Order.objects.get(id=pk) 
    if request.method == 'GET':
        context = {'order': o}
        return render(request, 'webkiosk/order_delete.html', context)
    elif request.method == 'POST':
        o.delete()
        return redirect('webkiosk:order-list')

# ------------------ CUSTOMER VIEWS ------------------

def customerlist(request):
    cl = Customer.objects.all()
    print(cl)
    context = {'customerlist': cl}
    return render (request, 'webkiosk/customer_list.html', context)

def createcustomer(request):
    if request.method == "GET":
        acf = AddCustomerForm()
    elif request.method == "POST":
        acf = AddCustomerForm(request.POST)
        # print(f)
        if acf.is_valid():
            acf.save()
            return redirect('webkiosk:customer-list')
        else:
            print('invalid form')

    context = {'form': acf, 'formheading': 'Add Customer'}
    return render (request, 'webkiosk/customer_form.html', context)

def updatecustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'GET':
        form = AddCustomerForm(instance=customer)
    elif request.method == 'POST':
        form = AddCustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Customer Profile Successfully Updated!')
    context = {'form':form,'formheading':'Update Customer'}
    return render(request, 'webkiosk/customer_form.html', context)

def deletecustomer(request, pk):
    c = Customer.objects.get(id=pk) 
    if request.method == 'GET':
        context = {'customer': c}
        return render(request, 'webkiosk/customer_delete.html', context)
    elif request.method == 'POST':
        c.delete()
        return redirect('webkiosk:customer-list')
    
def detailcustomer(request, pk):
    c = Customer.objects.get(id=pk)
    context = {'customer': c}
    return render(request, 'webkiosk/customer_detail.html', context)

def detailcustomerorder(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = Order.objects.filter(customer=customer)
    customerorders = CustomerOrder.objects.filter(order__in=orders)
    context = {'customer': customer, 'orders': orders, 'customerorders': customerorders}
    return render(request,'webkiosk/customerorder_detail.html', context)
