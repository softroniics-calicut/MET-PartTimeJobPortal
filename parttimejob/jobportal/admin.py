from django.contrib import admin
from .models import Student,Login1,Agency,Job,Application

# Register your models here.
admin.site.register(Student)
admin.site.register(Agency)
admin.site.register(Login1)
admin.site.register(Job)
admin.site.register(Application)