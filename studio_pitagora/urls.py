from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', include('pitagoraDev.urls')),
    path('admin/', admin.site.urls),
    path('', lambda req:redirect('pitagoraDev'))
]
