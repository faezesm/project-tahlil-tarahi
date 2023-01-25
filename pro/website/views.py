from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return render(request,'website/first.html')
 
def about(request):
    return render(request,'website/about.html')

def bofe(request):
   return render(request,'website/bofe.html')

def entazamat(request):
    return render(request,'website/entazamat.html')


def tasisat1(request):
   return render(request,'website/tasisat1.html')

def login(request):
   return render(request,'website/login.page.html')

def registery(request):
   return render(request,'website/registery.html')
