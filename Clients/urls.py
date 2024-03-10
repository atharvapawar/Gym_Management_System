# urls.py in your app directory
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('plan_list/', views.plan_list, name='plan_list'),
    path('plan_list/member_list/', views.member_list, name='member_list'),
    path('enquiry/', views.enquiry_list, name='enquiry'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
]