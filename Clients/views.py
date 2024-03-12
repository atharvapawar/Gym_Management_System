from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Plan, Member, Enquiry
from .forms import PlanFrom, MemberForm, EnquiryFrom, CustomUserRegistrationForm
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    plans = Plan.objects.all()
    return render(request, 'Clientsapp/home.html', {'plans': plans})

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, email=email, password=password)

            return redirect('login')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'Authorization/Register.html', {'form': form})

@csrf_exempt       
def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Handle invalid login
            # Redirect to login page with error message
            return redirect('login')
    return render(request, 'Authorization/login.html')

def my_logout(request):
    logout(request)
    return redirect('login')

def plan_view(request):
    plans = Plan.objects.all()
    return render(request, 'Clientsapp/Viewing/plan_view.html', {'plans': plans})

def view_members(request):
    members = Member.objects.all()
    return render(request, 'Clientsapp/Viewing/view_members.html', {'members': members})

def view_enquiry(request):
    enquiries = Enquiry.objects.all()
    return render(request, 'Clientsapp/Viewing/view_enquiry.html', {'enquiries': enquiries})

def add_plan(request):
    if request.method == 'POST':
        form = PlanFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plan_view')
    else:
        form = PlanFrom()
    return render(request, 'Clientsapp/Adding/add_plan.html', {'form': form})

def add_member(request):
    form = MemberForm() 
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)
            selected_plan = member.plan
            plan = Plan.objects.get(pk=selected_plan.pk)
            member.total_fees = plan.amount  
            form.save()  
            return redirect('view_members')
    return render(request, 'Clientsapp/Adding/add_member.html', {'form': form})

def add_enquiry(request):
    if request.method == 'POST':
        form = EnquiryFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_enquiry')
    else:
        form = EnquiryFrom()
    return render(request, 'Clientsapp/Adding/add_enquiry.html', {'form': form})

def remove_from_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)
    
    if request.method == 'POST':
        plan.delete()
        return redirect('plan_view')

    return render(request, 'Clientsapp/Viewing/plan_view.html')

def remove_from_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)
    
    if request.method == 'POST':
        member.delete()
        return redirect('view_members')

    return render(request, 'Clientsapp/Viewing/view_members.html')

def remove_from_enquiry(request, enquiry_id):
    enquiry = get_object_or_404(Enquiry, id=enquiry_id)

    if request.method == 'POST':
        enquiry.delete()
        return redirect('view_enquiry')

    return render(request, 'Clientsapp/Viewing/view_enquiry.html')
