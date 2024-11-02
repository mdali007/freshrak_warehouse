# account/admin.py
from django.contrib import admin
from .models import Staff, Task, Attendance

admin.site.register(Staff)
admin.site.register(Task)
admin.site.register(Attendance)