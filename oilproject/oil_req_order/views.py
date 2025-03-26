from django.shortcuts import render
from django.http import HttpResponse
from oil_req_order.models import Oil_req_order

# Create your views here.

def index(request):
    ###all_req = Oil_req_order.objects.filter(oil_amount=0) ##filter
    all_req = Oil_req_order.objects.all()
    return render(request,"index.html",{"all_req":all_req})

def about(request):
    return render(request,"about.html")

def form(request):
    return render(request,"form.html")