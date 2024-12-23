from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import welcome_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome_view, name='welcome'),
    path('home/', home_view, name='home'),
    #apps
    path('users/', include('users.urls')),
    path('workouts/', include('workouts.urls')),
    path('manual/', include('manual.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)