from django.shortcuts import render, redirect
from .models import UserDocuments,UserDocuments2,UserDocuments3
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# from django.http import HttpResponse

# http://127.0.0.1:8000/
# Create your views here.

@login_required(login_url="/")
def layout(request):
    return render(request,'layout.html')


@login_required(login_url="/")
def about(request):
    return render(request, 'pages/about.html')


def login(request):
    return render(request, 'pages/login.html')

@login_required(login_url="/")
def tables(request):

    if User.is_authenticated:


        dokumanlar = UserDocuments.objects.all().filter(userId=request.user.id)
        dokumanlar2 = UserDocuments2.objects.all().filter(userId=request.user.id)
        dokumanlar3 = UserDocuments3.objects.all().filter(userId=request.user.id)
        datas = {
            'dokumanlar':  dokumanlar,
            'dokumanlar2': dokumanlar2,
            'dokumanlar3':  dokumanlar3,
        }
    # return HttpResponse('<h1>Hello SisaSoft</h1>')

        return render(request, 'pages/tables.html',datas)



@login_required(login_url="/")
def members(request):
    calisanlar = User.objects.all()
    calisanlar_datas = {
        'calisanlar': calisanlar
    }
    return render(request, 'pages/members.html',calisanlar_datas)

@login_required(login_url="/")
def profile(request):
    return render(request, 'pages/profile.html')

@login_required(login_url="/")
def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            kullanici = form.save()
            update_session_auth_hash(request, kullanici)
            messages.success(request, "Şifreniz Başarıyla Güncellenmiştir!")

            return redirect('change-password')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'pages/change_password.html', context={
        'form' : form
    })


def myAdmin(request):
    return render(request, 'pages/myAdmin.html')
