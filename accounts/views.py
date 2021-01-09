from django.shortcuts import render, HttpResponse , redirect
from django.contrib import messages
from .forms import CreateUserForm
from product.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as gercek_login
from django.contrib.auth import logout as gercek_logout




# Create your views here.
def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request , username=username , password=password)
        if user is not None:
            gercek_login(request , user)
            return redirect('home')
        else:
            messages.info(request , 'Username or password is incorrect!')

    return render(request, 'login.html')


def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()


            newname = form.cleaned_data.get('username')
            newuser = User.objects.get(username=newname)
            messages.success(request, 'Account was created for ' + newname)
            Customer.objects.create(user=newuser, name=newuser.username, email=newuser.email)
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def logout(request):
    gercek_logout(request)
    return redirect('home')
