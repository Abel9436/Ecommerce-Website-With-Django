from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    products=models.Product.objects.all()
    catagory=models.Catagory.objects.all()
    context={
        'catagory':catagory,
        'products':products
    }
    return render(request,'ecommerceapp/index.html',context)