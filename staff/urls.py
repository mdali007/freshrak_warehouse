from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.staff_profile_view, name='staff_profile'),
    path('owner/', views.owner_dashboard_view, name='owner_dashboard'),
    path('attendance_view/', views.attendance_view, name='attendance_view'),
    path('dashboard/', views.overview_dashboard_view, name='overview_dashboard'),
]
