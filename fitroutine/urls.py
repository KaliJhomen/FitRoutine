from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import user_login
from .views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_login, name='login'),
    path('home/', home_view, name='home'),
    #apps
    path('users/', include('users.urls')),
    path('workouts/', include('workouts.urls')),
    path('manual/', include('manual.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)