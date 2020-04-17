from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('planning/', include('planning.urls')),
    path('forfait/', include('forfait.urls')),
]
