from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('layout', views.layout, name='layout'),
    path('about', views.about, name='about'),
    path('login',views.login, name='login'),
    path('tables',views.tables, name='tables'),
    path('members',views.members, name='members'),
    path('profile',views.profile, name='profile'),
    path('change-password',views.change_password, name='change-password'),
    # path('tables2',views.tables2, name='tables2'),
    # path('tables3',views.tables3, name='tables3'),
    path('myAdmin',views.myAdmin, name='myAdmin'),



]
# path('', views.index, name='index')