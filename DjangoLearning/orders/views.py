from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # response=HttpResponse("Hello from orders")
    response=render(request,'index.html')
    
    return response

