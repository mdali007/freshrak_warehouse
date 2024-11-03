from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a superuser if it doesn\'t exist'

    def handle(self, *args, **kwargs):
        username = 'admin'  # Choose your username
        password = 'admin123'  # Choose your password
        email = 'admin@example.com'  # Choose your email

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, password=password, email=email)
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} created successfully!'))
        else:
            self.stdout.write(self.style.WARNING(f'Superuser {username} already exists.'))