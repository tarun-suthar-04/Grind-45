from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    developed_by="TARUN SUTHAR"
    mentors=[
        "Football",
        "Cricket",
        "Basketball",
        "Baseball",
        "Hockey"]

    context={
        "developer":developed_by ,
        "mentors":mentors
    }
        # response=HttpResponse("Hello from orders")
    response=render(request,'index.html',context)
    
    return response

