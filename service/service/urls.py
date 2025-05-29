from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('api/v1/', include('services.urls', namespace='services')),
    path('admin/', admin.site.urls),
]
