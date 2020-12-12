from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm
# Create your views here.
def home(request):
    return render(request,'myapp/index1.html')

#about page
def about(request):
    return render(request,'myapp/about.html')

#contact page
def contact(request):
    return render(request,'myapp/contact.html')

#registration page of faculty
def reg(request):
    if request.method=="POST":
     fm = SignUpForm(request.POST)
     if fm.is_valid():
         fm.save()
         messages.success(request,'Your Account Has Been Created Succesfully!!')
    else:
        fm = SignUpForm()
    return render(request,'myapp/reg.html',{"forms":fm})
def charts(request):
    return render(request,'myapp/charts.html')

def index(request):
    return render(request,'myapp/index.html')

