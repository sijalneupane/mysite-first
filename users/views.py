from django.shortcuts import redirect, render
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Welcome {username}, your account is created')
            return redirect('login')
    else:
        form=RegisterForm()
    return render (request,'users/register.html',{'form':form,})

@login_required 
def profilepage(request):
    return render (request, 'users/profile.html')
