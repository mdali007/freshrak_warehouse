# staff/admin.py
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User
from staff.models import Staff, Task

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    # Staff Group
    staff_group, created = Group.objects.get_or_create(name='Staff')
    
    # Permissions for Staff Group
    content_type = ContentType.objects.get_for_model(Staff)
    
    # Get or create the required permissions
    view_staff_permission, _ = Permission.objects.get_or_create(
        codename='view_staff',
        name='Can view staff',
        content_type=content_type
    )
    
    change_staff_permission, _ = Permission.objects.get_or_create(
        codename='change_staff',
        name='Can change staff',
        content_type=content_type
    )
    
    staff_group.permissions.add(view_staff_permission, change_staff_permission)
    
    # Owner Group
    owner_group, created = Group.objects.get_or_create(name='Owner')
    
    # Get or create the required permissions for Owner Group
    owner_view_staff_permission, _ = Permission.objects.get_or_create(
        codename='view_staff',
        name='Can view staff'
    )
    
    change_task_permission, _ = Permission.objects.get_or_create(
        codename='change_task',
        name='Can change task',
        content_type=ContentType.objects.get_for_model(Task)
    )
    
    owner_group.permissions.add(owner_view_staff_permission, change_task_permission)
    
    # Main Admin Group (Superuser)
    admin_group, created = Group.objects.get_or_create(name='MainAdmin')
    admin_group.permissions.add(*Permission.objects.all())  # Full permissions
