from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from staff.models import Staff, Task, Attendance
from django.utils import timezone
from django.shortcuts import get_object_or_404
from product.models import Product
import datetime 

# Staff view - Can view and edit their own profile and tasks
@login_required
def staff_profile_view(request):
    staff = Staff.objects.get(user=request.user)
    all_tasks = Task.objects.filter(staff=staff)
    
    # Filter today's tasks and scheduled tasks
    today = timezone.now().date()
    todays_tasks = all_tasks.filter(scheduled_date=today)
    scheduled_tasks = all_tasks.exclude(scheduled_date=today)

    if request.method == 'POST':
        if 'profile_picture' in request.FILES:
            staff.profile_picture = request.FILES['profile_picture']
            staff.save()
        
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        task.completed = True
        task.note = request.POST.get('note', '')
        task.save()
        
        return redirect('staff_profile')

    return render(request, 'staff_profile.html', {
        'staff': staff,
        'todays_tasks': todays_tasks,
        'scheduled_tasks': scheduled_tasks,
    })



@login_required
def check_in_view(request):
    staff = Staff.objects.get(user=request.user)

    # Check if the staff member has already checked in today
    today = timezone.now().date()
    attendance, created = Attendance.objects.get_or_create(staff=staff, date=today)

    if request.method == 'POST' and not attendance.check_in_time:
        # Only update check-in if it hasn't been set
        attendance.check_in_time = timezone.now()
        attendance.save()
        return redirect('staff_profile')

    return render(request, 'staff_profile.html', {'staff': staff, 'attendance': attendance})


@login_required
def check_out_view(request):
    staff = Staff.objects.get(user=request.user)

    # Check if the staff member has checked in today
    today = timezone.now().date()
    attendance = get_object_or_404(Attendance, staff=staff, date=today)

    if request.method == 'POST' and attendance.check_in_time and not attendance.check_out_time:
        # Only update check-out if it hasn't been set
        attendance.check_out_time = timezone.now()
        attendance.save()
        return redirect('staff_profile')

    return render(request, 'staff_profile.html', {'staff': staff, 'attendance': attendance})



# Owner view - Can view all staff profiles and assign tasks
@login_required
@user_passes_test(lambda u: u.groups.filter(name='Owner').exists())
def owner_dashboard_view(request):
    all_staff = Staff.objects.all()
    tasks = Task.objects.all()  # Get all tasks

    # Fetch attendance records for today
    today = timezone.now().date()
    attendance_records = Attendance.objects.filter(date=today)

    if request.method == 'POST':
        task_description = request.POST.get('task_description')
        staff_id = request.POST.get('staff_id')
        action = request.POST.get('action')

        if action == 'assign':  # Assign new task
            staff_member = get_object_or_404(Staff, id=staff_id)
            Task.objects.create(staff=staff_member, task_name=task_description)
        elif action == 'delete':  # Delete a task
            task_id = request.POST.get('task_id')
            task = get_object_or_404(Task, id=task_id)
            task.delete()

    return render(request, 'owner_dashboard.html', {
        'all_staff': all_staff, 
        'tasks': tasks,
        'attendance_records': attendance_records  # Pass attendance records to the template
    })





@login_required
@user_passes_test(lambda u: u.groups.filter(name='Owner').exists())
def overview_dashboard_view(request):
    all_staff_count = Staff.objects.count()  # Number of staff members
    # Assuming there's a Product model with a date field to track yesterday's stats
    # yesterday_product_stats = Product.objects.filter(date=datetime.date.today() - datetime.timedelta(days=1))

    return render(request, 'owner_overview.html', {
        'all_staff_count': all_staff_count,
        # 'yesterday_product_stats': yesterday_product_stats,
    })
