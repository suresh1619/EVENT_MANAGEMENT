# urls.py

from django.urls import path
from .views import send_email

urlpatterns = [
    path('contact/', send_email, name='send_email'),
]
