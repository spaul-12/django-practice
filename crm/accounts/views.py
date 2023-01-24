from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    customer=Customer.objects.all()
    order = Order.objects.all()
    total_order = order.count()
    delivered = order.filter(status="Delivered").count()
    pending = order.filter(status="Pending").count()
    context= {
        "customer":customer,
        "order": order,
        "total_order":total_order,
        "delivered":delivered,
        "pending":pending
    }

    return render(request , 'accounts/home.html',context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':

            username=request.POST.get('username')
            password=request.POST.get('password')

            user = authenticate(request,username=username,password=password)
            
            if user is not None:
                login(request,user)
                return redirect(home)

        context={}    
    
        return render(request,'accounts/login.html',context)
    
def logoutuser(request):
    logout(request)
    return redirect('login')
  


def register(request):
    form = CreateUserForm()

    if request.method=="POST":
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
            
    context = {
        "form":form
    }

    return render(request,'accounts/register.html',context)
     


def customer(request,pk):
    customer=Customer.objects.get(id=pk)
    order = customer.order_set.all()
    #print(request.GET)
    myform = OrderFilter(request.GET, queryset=order)
    order=myform.qs
    total = customer.order_set.count()
    context = {
        "customer":customer,
        "total":total,
        "order":order,
        "myform":myform
    }
    return render(request, 'accounts/customer.html',context)

def createorder(request):
    form =OrderForm()  
    if request.method=='POST':
        #print("printing the form ",request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    frontend = {
        "form":form
    }
    return render(request,'accounts/order.html',frontend)

def updateorder(request,id):
    order=Order.objects.get(id=id)
    form = OrderForm(instance=order)   
    if request.method=='POST':
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={
        "form":form
    }
    return render(request,'accounts/order.html',context)

def deleteorder(request,pk):
    order=Order.objects.get(id=pk)
    context={
        "order":order
    }
    if request.method=="POST":
        order.delete()
        return redirect("/")
    
    return render(request,'accounts/remove.html',context)