from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.staff_profile_view, name='staff_profile'),
    path('owner/', views.owner_dashboard_view, name='owner_dashboard'),
    path('check-in/', views.check_in_view, name='check_in_view'),
    path('check-out/', views.check_out_view, name='check_out_view'),
    path('dashboard/', views.overview_dashboard_view, name='overview_dashboard'),
]
