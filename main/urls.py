from django.contrib import admin ## 
from django.urls import path, include ## 
from . import views
import accounts.views 
app_name = 'main'

urlpatterns = [
    path('', views.main, name = 'main'),
    path('trendingnow/', views.trendingnow, name ='trendingnow'),
    path('c1/', views.c1, name = 'c1'),
    path('c2/', views.c2, name = 'c2'),
    path('c3/', views.c3, name = 'c3'), 
    path('accounts/', include('accounts.urls')), ## 
    ]