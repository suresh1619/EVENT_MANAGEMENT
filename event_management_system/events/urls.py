from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_events, name='list_events'),
    path('event/<int:pk>/', views.view_event, name='view_event'),
    path('event/new/', views.create_new_event, name='create_new_event'),
    path('event/<int:pk>/delete/', views.remove_event, name='remove_event'),
    path('event/<int:pk>/update/', views.update_event, name='update_event'),
    path('event/<int:pk>/rsvp/', views.rsvp_to_event, name='rsvp_to_event'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login')
]
