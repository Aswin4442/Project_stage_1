from django.urls import path
from techapp import views


urlpatterns = [
    path('',views.index,name='index'),
    path('product/',views.product,name='product'),
    path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact'),
    path('user/',views.user,name='user'),
    path('cart/',views.cart,name='cart'),
    path('register/',views.register,name='register'),
    path('checkout/',views.checkout,name='checkout'),
    path('address/',views.address,name='address'),
    path('orders/',views.orders,name='orders'),
    path('user_login/', views.user_login, name='user_login'),  # Login view
    path('watch/',views.watch,name='watch'),
    path('headphone/',views.headphone,name='headphone'),
    path('speaker/',views.speaker,name='speaker'),
    path('joystick/',views.joystick,name='joystick'),
    path('contact_view/', views.contact_view, name='contact_view'),
    path('contactlist/', views.contactlist, name='contactlist'),
    # path('my_account/', views.my_account, name='my_account'),
    path('things/<int:product_id>/',views.product_detail,name='product_detail'),

]