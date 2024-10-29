from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('staff/', include('staff.urls')),  # Include staff app URLs
    path('account/', include('account.urls')),  # Include account app URLs
    path('product/', include('product.urls')), 
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
