
from django.contrib import admin
from django.urls import path
from hospitalapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.index, name='index'),
    path('service/', views.service, name='service'),
    path('starter/', views.service, name='starter'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('show/', views.appointment, name='show'),
    path('', views.register, name='register'),
    path('login/', views.login_view, name='login'),

#mpesa API
    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),

]
