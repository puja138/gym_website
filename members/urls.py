from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trainers/', views.trainers, name='trainers'),
    path('plans/', views.plans, name='plans'),
    path('schedule/', views.schedule, name='schedule'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),

    path('join-now/<str:plan_name>/', views.join_now, name='join_now'),
    path('join-success/', views.join_success, name='join_success'),
    path('payment-success/', views.payment_success, name='payment_success'),
]
