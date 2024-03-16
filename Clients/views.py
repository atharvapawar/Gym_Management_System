#from http import client
import razorpay
from django.conf import settings
from .models import *
from .forms import *
from django.shortcuts import *
from django.contrib.auth import *
from django.contrib import messages
from django.contrib.auth.models import *
from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    plans = Plan.objects.all()
    if request.method == 'POST':
        form = EnquiryFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EnquiryFrom()
    return render(request, 'Clientsapp/home.html', {'form': form ,'plans': plans} )

################### Authentications###################
def register(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = CustomUserRegistrationForm()
    return render(request, 'Authorization/Register.html', {'form': form})
      
def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password. Please try again or return to the home page and use the enquiry section to inform us.')
            return redirect('login')
    return render(request, 'Authorization/login.html')

def my_logout(request):
    logout(request)
    return redirect('login')

################### Payment ###################

# Create a new view for payment confirmation
def proceed_to_pay(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)
    return render(request, 'Clientsapp/Payment/proceed_to_pay.html', {'plan': plan})

def payment_confirmation(request, plan_id):
    plan = get_object_or_404(Plan, pk=plan_id)
    client = razorpay.Client(auth=(settings.RAZORPAY_TEST_KEY_ID, settings.RAZORPAY_TEST_KEY_SECRET))
    order_amount = (plan.amount * 100)
    order_currency = 'INR'
    
    order = client.order.create({'amount':order_amount, 'currency':order_currency})

    context = {'order_amount': order_amount, 'order': order, 'razorpay_key_id': settings.RAZORPAY_TEST_KEY_ID}
    return render(request, 'Clientsapp/Payment/payment_confirmation.html', {'plan': plan, **context})

################### Search ###################
def plan_results(request):
    plan_query = request.GET.get('plan_search', '')
    plans = Plan.objects.filter(name__icontains=plan_query)
    return render(request, 'Clientsapp/Viewing/plan_view.html', {'plans': plans, 'plan_query': plan_query})

def member_results(request):
    member_query = request.GET.get('member_search', '')
    members = Member.objects.filter(name__icontains=member_query)
    return render(request, 'Clientsapp/Viewing/view_members.html', {'members': members, 'member_query': member_query})

def enquiry_results(request):
    enquiry_query = request.GET.get('enquiry_search', '')
    enquiries = Enquiry.objects.filter(name__icontains=enquiry_query)
    return render(request, 'Clientsapp/Viewing/view_enquiry.html', {'enquiries': enquiries, 'enquiry_query': enquiry_query})

################### View ###################
def plan_view(request):
    plans = Plan.objects.all()
    return render(request, 'Clientsapp/Viewing/plan_view.html', {'plans': plans})

def view_members(request):
    members = Member.objects.all()
    return render(request, 'Clientsapp/Viewing/view_members.html', {'members': members})

def view_enquiry(request):
    enquiries = Enquiry.objects.all()
    return render(request, 'Clientsapp/Viewing/view_enquiry.html', {'enquiries': enquiries})

################### Add ###################
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
    plans = Plan.objects.all()  # Get all available plans
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)
            selected_plan_id = request.POST.get('plan')  # Get the selected plan ID from the form
            plan = Plan.objects.get(pk=selected_plan_id)
            member.total_fees = plan.amount
            member.save()
            # Redirect to the payment confirmation page with the selected plan ID
            return redirect('proceed_to_pay', plan_id=selected_plan_id)
    else:
        form = MemberForm()
    return render(request, 'Clientsapp/Adding/add_member.html', {'form': form, 'plans': plans})

def add_enquiry(request):
    if request.method == 'POST':
        form = EnquiryFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_enquiry')
    else:
        form = EnquiryFrom()
    return render(request, 'Clientsapp/Adding/add_enquiry.html', {'form': form})

################### Update ###################
def update_plan(request, id):
    plan = get_object_or_404(Plan, id=id)
    if request.method == 'POST':
        form = PlanFrom(request.POST, instance=plan)
        if form.is_valid():
            form.save()
            return redirect('plan_view')
    else:
        form = PlanFrom(instance=plan)

    return render(request, 'Clientsapp/Updating/update_plan.html', {'form': form})

def update_member(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('view_members')
        else:
            form = MemberForm(instance=member)
        
        return render(request, 'Clientsapp/Updating/update_member.html', {'form': form})

################### Delete ###################
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

