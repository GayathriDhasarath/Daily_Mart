from django.shortcuts import render,redirect
from Adminapp.models import *
from .models import *
from django.db.models import Sum

# Create your views here.
def userindex(request):
    u=request.session.get('uid')
    data=Products.objects.all()
    cartnum=Cart.objects.filter(userid=u,status=0).count()
    return render(request,'userindex.html',{'data':data,'cartnum':cartnum})
def contact(request):
    u=request.session.get('uid')
    cartnum=Cart.objects.filter(userid=u,status=0).count()
    return render(request,'contact.html',{'cartnum':cartnum})
def contact_submit(request):
    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        subject=request.POST['subject']
        message=request.POST['message']
        data=Contact_details(name=name,email=email,phone=phone,subject=subject,message=message)
        data.save()
        return redirect('userindex')

def login(request):
    
    return render(request,'login.html')
def register(request):
    if(request.method=="POST"):
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        address=request.POST['address']
        data=Users_registration(name=name,email=email,phone=phone,password=password,confirm_password=confirm_password,Address=address)
        data.save()
        return redirect('userindex')
    return render(request,'register.html')
def logindata(request):
    if(request.method=='POST'):
        username=request.POST['uname']
        password=request.POST['password']
        if Users_registration.objects.filter(name=username,password=password).exists():
            data=Users_registration.objects.filter(name=username,password=password).values('email','phone','Address','id').first()
            request.session['email']=data['email']
            request.session['phone']=data['phone']
            request.session['address']=data['Address']
            request.session['uname']=username
            request.session['password']=password
            request.session['uid']=data['id']
            return redirect('userindex')
        else:
            return redirect('login',{'msg':"Invalid Credentials"})
    else:
        return redirect('userindex')
def logout(request):
    del request.session['uname']
    del request.session['password']
    del request.session['email']
    del request.session['phone']
    del request.session['address']
    del request.session['uid']
    return redirect('userindex')
def shop(request):
    u=request.session.get('uid')
    data=Products.objects.all()
    cartnum=Cart.objects.filter(userid=u,status=0).count()
    return render(request,'shop.html',{'data':data,'cartnum':cartnum})
def cart(request):
    u=request.session.get('uid')
    cartnum=Cart.objects.filter(userid=u,status=0).count()
    data=Cart.objects.filter(userid=u,status=0)
    s=Cart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    return render(request,'cart.html',{'data':data,'s':s,'cartnum':cartnum})
def addtocart(request,id):
    if (request.method=="POST"):
        userid2=request.session.get('uid')
        quantity2=request.POST['quantity']  
        total=request.POST['total']     
        data=Cart(userid=Users_registration.objects.get(id=userid2),productid=Products.objects.get(id=id),quantity=quantity2,total=total)
        data.save()
        return redirect('cart')
def singleproduct(request,id):
    u=request.session.get('uid')
    cartnum=Cart.objects.filter(userid=u,status=0).count()
    data=Products.objects.filter(id=id)
    data2=Products.objects.all()
    return render(request,'singleproduct.html',{'data':data,'data2':data2,'cartnum':cartnum})
def remove(request,id):
    Cart.objects.filter(id=id).delete()
    return redirect('cart')
def checkout(request):
    u=request.session.get('uid')
    cartnum=Cart.objects.filter(userid=u,status=0).count()
    s=Cart.objects.filter(userid=u,status=0).aggregate(Sum('total'))
    data=Cart.objects.filter(userid=u,status=0)
    return render(request,'checkout.html',{'data':data,'s':s,'cartnum':cartnum})
def checkoutdata(request):
    if request.method=="POST":
        u=request.session.get('uid')
        address1=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        zipcode=request.POST['zipcode']
        order=Cart.objects.filter(userid=u,status=0)

        for i in order:
            data=Checkout(userid=Users_registration.objects.get(id=u),cartid=Cart.objects.get(id=i.id),address=address1,city=city,state=state,country=country,zipcode=zipcode)
            data.save()
            Cart.objects.filter(id=i.id).update(status=1)
    return redirect('userindex')

       


    


