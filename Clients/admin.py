from django.contrib import admin
from . models import Plan,Member, Enquiry

# Register your models here.
admin.site.register(Plan)

admin.site.register(Member)

admin.site.register(Enquiry)