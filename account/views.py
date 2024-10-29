from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Login view
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                
                # Check the user's group and redirect accordingly
                if user.groups.filter(name='Staff').exists():
                    return redirect('staff_profile')  # Redirect to staff profile
                elif user.groups.filter(name='Owner').exists():
                    return redirect('overview_dashboard')  # Redirect to owner dashboard
                elif user.is_superuser:
                    return redirect('/admin/')  # Redirect superuser to admin panel
                
                # If no group, fallback to a default page
                return redirect('staff_profile')  # Default redirection (can be changed)
    else:
        form = AuthenticationForm()
    
    return render(request, 'index.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login after logout