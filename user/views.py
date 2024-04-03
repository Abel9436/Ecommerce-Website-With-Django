from django.shortcuts import render

# Create your views her
def profile(request):
    return render (request,'user/index.html')