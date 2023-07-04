from django.shortcuts import render,redirect
from .models import*
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from Userapp.models import *

# Create your views here.
def adminindex(request):
    products=Products.objects.all().count()
    users=Users_registration.objects.all().count()
    orders=Checkout.objects.all().count()
    message=Contact_details.objects.all().count()
    return render(request,'adminindex.html',{'products':products,'users':users,'orders':orders,'message':message})
def productsform(request):
    return render(request,'productsform.html')
def products(request):
    if (request.method=='POST'):
        product_name=request.POST['product_name']
        product_type=request.POST['product_type']
        product_desc=request.POST['product_desc']
        product_category=request.POST['product_category']
        product_price=request.POST['product_price']
        product_image=request.FILES['product_image']
        data=Products(product_name=product_name,product_type=product_type,product_desc=product_desc,product_category=product_category,product_price=product_price,product_image=product_image)
        data.save()
        return redirect('productstable')
def productstable(request):
    data=Products.objects.all()
    return render(request,'productstable.html',{'data':data})
def product_delete(request,id):
    Products.objects.filter(id=id).delete()
    return redirect('productstable')
def editdisplay(request,id):
    data=Products.objects.filter(id=id)
    return render(request,'productsedit.html',{'data':data})
def productsedit(request,id):
    if (request.method=='POST'):
        product_name=request.POST['product_name']
        product_type=request.POST['product_type']
        product_desc=request.POST['product_desc']
        product_category=request.POST['product_category']
        product_price=request.POST['product_price']
        try:
            image=request.FILES['product_image']
            fs=FileSystemStorage()
            file=fs.save(image.name,image)
        except MultiValueDictKeyError:
            file=Products.objects.get(id=id).product_image
        Products.objects.filter(id=id).update(product_name=product_name,product_type=product_type,product_desc=product_desc,product_category=product_category,product_price=product_price,product_image=file)
        return redirect('productstable')
def usermessage(request):
    data=Contact_details.objects.all()
    return render(request,'usermessage.html',{'data':data})




