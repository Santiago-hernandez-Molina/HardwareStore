from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def login_v(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username,password=password)
        print(user)

        if user:
            login(request,user)
            return redirect('/products')
        else:
             return render(request,'users/login.html',{'error':'invalid username or password'})
    return render(request,'users/login.html')

def logout_v(request):
    logout(request)
    return redirect('login')