from django.urls import path
from .import views

urlpatterns = [
    path('userindex/',views.userindex,name='userindex'),
    path('contact/',views.contact,name='contact'),
    path('contact_submit/',views.contact_submit,name='contact_submit'),
    path('cart/',views.cart,name='cart'),
    path('login/',views.login,name='login'),   
    path('register/',views.register,name='register'), 
    path('logindata/',views.logindata,name='logindata'),     
    path('logout/',views.logout,name='logout'),
    path('shop/',views.shop,name='shop'),
    path('addtocart/<int:id>/',views.addtocart,name='addtocart'),
    path('singleproduct/<int:id>/',views.singleproduct,name='singleproduct'),
    path('remove/<int:id>/',views.remove,name='remove'),
    path('checkout/',views.checkout,name='checkout'),
    path('checkoutdata/',views.checkoutdata,name='checkoutdata')
]
