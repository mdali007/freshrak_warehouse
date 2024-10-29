# staff/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django's User model
    full_name = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    passport_number = models.CharField(max_length=20)
    visa_status = models.CharField(max_length=50)
    visa_expiry_date = models.DateField()

    def __str__(self):
        return self.full_name

    class Meta:
        # Use unique permission names
        permissions = [
            ('can_view_staff', 'Can view staff'),
            ('can_change_staff', 'Can change staff'),
        ]


class Task(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    assigned_date = models.DateField(auto_now_add=True)
    scheduled_date = models.DateTimeField(default=timezone.now) 
    completed = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.task_name} - {self.staff.full_name}"


class Attendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)  # Add check-out time
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.staff.full_name} - {self.date} - {'Present' if self.is_present else 'Absent'}"