from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('clothing',views.clothing, name = 'clothing'),
    path('accessories',views.accessories, name = 'accessories'),
    path('cart', views.cart, name = 'cart'),
    path('updatecart',views.updateCart),
    path('updatequantity',views.updateQuantity),
    path('checkout', views.checkout, name = 'checkout'),
    path('add-address', views.add_address, name = 'add_address'),
    path('order-done',views.order_done,name='done'),
    
    

    # path('register/', views.register, name='register'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
]