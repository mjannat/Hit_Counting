from django.contrib import admin

# Register your models here.
from .models import Student,User

admin.site.register(Student)
admin.site.register(User)
