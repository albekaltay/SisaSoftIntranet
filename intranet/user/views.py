from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request,f"SisaSoft Intranet'e Hoşgeldin {request.user.first_name}!")

            return redirect('about')
        else:
            messages.warning(request,('Kullanıcı Adınız veya Parolanız Yanlış!'))
            return redirect('login')
    else:
        return render(request, 'user/login.html')



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('login')