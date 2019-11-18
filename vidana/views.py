from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        _username   = request.POST.get('username')
        _password = request.POST.get('password')
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return render(request, "demo.html")
    return render(request, "login.html")


@login_required(login_url = 'login')
def logout_view(request):
    logout(request)
    return render(request, "login.html")
