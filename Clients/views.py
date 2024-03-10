from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Plan, Member, Enquiry
from .forms import PlanFrom, MemberForm, EnquiryFrom

def home(request):
    return render(request, 'Clientsapp/home.html')

def plan_view(request):
    plans = Plan.objects.all()
    return render(request, 'Clientsapp/plan_view.html', {'plans': plans})

def add_plan(request):
    if request.method == 'POST':
        form = PlanFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plan_view')
    else:
        form = PlanFrom()
    return render(request, 'Clientsapp/add_plan.html', {'form': form})

def view_members(request):
    members = Member.objects.all()
    return render(request, 'Clientsapp/view_members.html', {'members': members})

def add_member(request):
    form = MemberForm() 
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)  # Don't save to DB yet
            selected_plan = member.plan
            plan = Plan.objects.get(pk=selected_plan.pk)
            member.total_fees = plan.amount  # Set total_fees based on selected plan
            form.save()  # Now save the form along with the calculated total_fees
            return redirect('view_members')
    return render(request, 'Clientsapp/add_member.html', {'form': form})

def view_enquiry(request):
    enquiries = Enquiry.objects.all()
    return render(request, 'Clientsapp/view_enquiry.html', {'enquiries': enquiries})

def add_enquiry(request):
    if request.method == 'POST':
        form = EnquiryFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_enquiry')
    else:
        form = EnquiryFrom()
    return render(request, 'Clientsapp/add_enquiry.html', {'form': form})

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
