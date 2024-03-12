# urls.py in your app directory
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_plan/', views.add_plan, name='add_plan'),
    path('plan_view/', views.plan_view, name='plan_view'),
    path('remove_from_plan/<int:plan_id>/', views.remove_from_plan, name='remove_from_plan'),
    path('remove_from_member/<int:member_id>/', views.remove_from_member, name='remove_from_member'),
    path('remove_from_enquiry/<int:enquiry_id>/', views.remove_from_enquiry, name='remove_from_enquiry'),
    path('add_member/', views.add_member, name='add_member'),
    path('view_members/', views.view_members, name='view_members'),
    path('add_enquiry/', views.add_enquiry, name='add_enquiry'),
    path('view_enquirys/', views.view_enquiry, name='view_enquiry'),
    path('register/', views.register, name='register'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
]
