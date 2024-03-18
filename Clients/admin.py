from django.contrib import admin
from . models import *

# Register your models here.
admin.site.site_header = "PowerFit Admin-Panel"

admin.site.register(Plan)

admin.site.register(Member)

admin.site.register(Enquiry)