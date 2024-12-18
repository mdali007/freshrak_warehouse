# Generated by Django 5.1.2 on 2024-10-24 05:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(default='default.jpg', upload_to='profile_pics/')),
                ('contact_number', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('passport_number', models.CharField(max_length=20)),
                ('visa_status', models.CharField(max_length=50)),
                ('visa_expiry_date', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=200)),
                ('assigned_date', models.DateField(auto_now_add=True)),
                ('scheduled_date', models.DateField()),
                ('completed', models.BooleanField(default=False)),
                ('note', models.TextField(blank=True, null=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staff')),
            ],
        ),
    ]
