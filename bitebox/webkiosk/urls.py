from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'webkiosk'

urlpatterns = [
    # http://localhpost:8000/webkiosk/
    path('', views.index, name='index'),
    path('testview/', views.testview, name='testview'),

    # http://localhost:8000/webkiosk/login/
    path('login/', views.login_page, name='login'),

    # http://localhost:8000/webkiosk/logout/
    path('logout/', auth_views.LogoutView.as_view(next_page='webkiosk:login'), name='logout'),

    #-------------------- FOOD URLS --------------------

    # http://localhpost:8000/webkiosk/menu/
    path('menu/', views.listfood, name='food-list'),

    # http://localhpost:8000/webkiosk/food/new/
    path('food/new/', views.createfood, name='food-create'),

    # http://localhost:8000/webkiosk/food/1/
    path('food/<int:pk>/', views.detailfood, name='food-detail'),

    # http://localhost:8000/webkiosk/food/1/edit
    path('food/<int:pk>/edit/', views.updatefood, name='food-update'),

    # http://localhost:8000/webkiosk/food/1/delete
    path('food/<int:pk>/delete/', views.deletefood, name='food-delete'),

    #-------------------- ORDER URLS --------------------
  
    # http://localhost:8000/webkiosk/orderform/
    path('orderform/', views.createorder, name='food-order'),

    # http://localhost:8000/webkiosk/orderform/1/
    path('orderform/<int:pk>/', views.customerorder, name='customer-order'),

    # http://localhpost:8000/webkiosk/order/1/
    path('order/<int:pk>/', views.detailorder, name='order-detail'),

    # http://localhpost:8000/webkiosk/orderlist/
    path('orderlist/', views.listorder, name='order-list'),

    # http://localhost:8000/webkiosk/order/1/edit
    path('order/<int:pk>/edit/', views.customerorder, name='order-update'),

    # http://localhost:8000/webkiosk/order/1/delete
    path('order/<int:pk>/delete/', views.deleteorder, name='order-delete'),

    #-------------------- CUSTOMER URLS --------------------
    
    # http://localhpost:8000/webkiosk/customer/
    path('customer/', views.customerlist, name='customer-list'),
    
    # http://localhpost:8000/webkiosk/customer/new/
    path('customer/new/', views.createcustomer, name='customer-create'),
   
    # http://localhost:8000/webkiosk/customer/1/edit
    path('customer/<int:pk>/edit/', views.updatecustomer, name='customer-update'),

    # http://localhost:8000/webkiosk/customer/1/delete
    path('customer/<int:pk>/delete/', views.deletecustomer, name='customer-delete'),

    # http://localhpost:8000/webkiosk/customer/new/
    path('customer/<int:pk>/', views.detailcustomer, name='customer-detail'),

    # http://localhpost:8000/webkiosk/customerorder/1/
    path('customerorder/<int:pk>/', views.detailcustomerorder, name='customerorder-detail'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)