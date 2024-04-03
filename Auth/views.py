from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signin(requst):
    if requst.method=='POST':
        email=requst.POST.get('email')
        password=requst.POST.get('password')
        user = authenticate(requst,username=email, password=password)
        if user is not None:
            login(requst, user)
            print('logged in')
            context={
                'email':email
            }
            return render(requst,'ecommerceapp/index.html',)
    messages.error(requst, 'Incorrect username or password and')        
    return render(requst,'Auth/index.html')
def signout(requst):
    logout(requst)
    return render(requst,'ecommerceapp/index.html')