from django.shortcuts import render
from django.http import HttpResponse

def  index(request):
    return render(request,"base.html")

def about(request):
    return render(request,"about.html")

def contscts(request):
    return render(request,"contacts.html")


