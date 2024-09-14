from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class EventDetail(models.Model):
    event_title = models.CharField(max_length=200)
    event_description = models.TextField()
    event_date = models.DateTimeField()
    event_location = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_title

class AttendeeRecord(models.Model):
    attendee_user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_detail = models.ForeignKey(EventDetail, on_delete=models.CASCADE)
    attended_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.attendee_user.username} - {self.event_detail.event_title}'

class UserActivityLog(models.Model):
    activity_user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_description = models.CharField(max_length=200)
    activity_timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.activity_user.username} - {self.activity_description}'

class login_details(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
class Signup_aten(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    Education = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
