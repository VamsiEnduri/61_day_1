from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(request):
    return HttpResponse("this is about view") # str

def contact(request):
    return HttpResponse("this is contact view") # str    

def login (request):
    return   render(request,"login.html") # 2 values  1(req) 2(html page)  
