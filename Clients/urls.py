from django.urls import path
from . import views

# create views and then add the views pages to the path
urlpatterns = [
    
    path('', views.home, name='home'),
    ################### Authentications###################
    path('register/', views.register, name='register'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout'),
    ################### Views ###################
    path('plan_view/', views.plan_view, name='plan_view'),
    path('view_members/', views.view_members, name='view_members'),
    path('view_enquirys/', views.view_enquiry, name='view_enquiry'),
    ################### Search ###################
    path('plan_search/',views.plan_results, name = 'plan_results'),
    path('member_search/',views.member_results, name='member_results'),
    #path('enquiry_search/',views.enquiry_results, name='enquiry_results'),
    ################### Adds ###################
    path('add_plan/', views.add_plan, name='add_plan'),
    path('add_member/', views.add_member, name='add_member'),
    path('add_enquiry/', views.add_enquiry, name='add_enquiry'),
    ################### Update ###################
    ################### Delete ###################
    path('remove_from_plan/<int:plan_id>/', views.remove_from_plan, name='remove_from_plan'),
    path('remove_from_member/<int:member_id>/', views.remove_from_member, name='remove_from_member'),
    path('remove_from_enquiry/<int:enquiry_id>/', views.remove_from_enquiry, name='remove_from_enquiry'),
    ################### Payment ###################

]
