from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Plan, Member, Enquiry
from .forms import MemberForm, EnquiryFrom

# Create your views here.
def home(request):
    return render(request, 'Clientsapp/home.html')

def plan_list(request):
    plans = Plan.objects.all()
    return render(request, 'Clientsapp/plan_list.html', {'plans': plans})

def member_list(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'Clientsapp/member_list.html', {'form': form})

def enquiry_list(request):
    if request.method == 'POST':
        form = EnquiryFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('enquiry_list')
    else:
        form = EnquiryFrom()
    return render(request, 'Clientsapp/enquiry.html', {'form': form})

def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    
    return render(request, 'Clientsapp/login.html')

def my_logout(request):
    logout(request)
    return redirect('login')
