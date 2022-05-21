from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect

def login(request):
   
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
      
        if User.objects.filter(email=email).filter():
           
            username = User.objects.filter(email=email).values_list(
                'username', flat=True).get()
            user = auth.authenticate(
                request,
                username=username,
                password=password)
         
            if user is not None:
                auth.login(request, user)
                return redirect('index')
       
    return render(request, 'login.html')