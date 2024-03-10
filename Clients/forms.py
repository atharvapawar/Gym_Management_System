# forms.py
from django import forms
from .models import Plan, Member, Enquiry

class PlanFrom(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'amount', 'duration']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'}),
        }

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'phone', 'email', 'age', 'gender', 'plan']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'plan': forms.Select(attrs={'class': 'form-control'}),
            'enrolled_on': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class EnquiryFrom(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }

