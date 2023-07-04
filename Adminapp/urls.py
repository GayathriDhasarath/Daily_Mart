
from django.urls import path
from .import views

urlpatterns = [
    path('',views.adminindex,name='adminindex'),
    path('productsform/',views.productsform,name='productsform'),
    path('products/',views.products,name='products'),
    path('productstable/',views.productstable,name='productstable'),
    path('product_delete/<int:id>/',views.product_delete,name='product_delete'),
    path('productsedit/<int:id>/',views.productsedit,name='productsedit'),
    path('editdisplay/<int:id>/',views.editdisplay,name='editdisplay'),
    path('usermessage/',views.usermessage,name='usermessage'),

]
