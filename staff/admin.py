# account/admin.py
from django.contrib import admin
from .models import Staff, Task

admin.site.register(Staff)
admin.site.register(Task)
