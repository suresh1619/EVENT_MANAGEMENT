from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.utils import timezone
from .models import EventDetail, AttendeeRecord, UserActivityLog,Signup_aten

def create_new_event(request):
    if request.method == 'POST':
        title = request.POST.get('event_title')
        description = request.POST.get('event_description')
        date = request.POST.get('event_date')
        location = request.POST.get('event_location')
        if title and description and date and location:
            new_event = EventDetail(
                event_title=title,
                event_description=description,
                event_date=date,
                event_location=location,
                created_on=timezone.now(),
                updated_on=timezone.now()
            )
            new_event.save()
            return redirect('list_events')
        else:
            return HttpResponse("Please provide all required fields.")
    return render(request, 'create_event_form.html')

def list_events(request):
    events = EventDetail.objects.all()
    return render(request, 'event_list.html', {'events': events})

def view_event(request, pk):
    event = get_object_or_404(EventDetail, pk=pk)
    return render(request, 'event_detail.html', {'event': event})

def remove_event(request, pk):
    event = get_object_or_404(EventDetail, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('list_events')
    return render(request, 'confirm_delete_event.html', {'event': event})

def update_event(request, pk):
    event = get_object_or_404(EventDetail, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('event_title')
        description = request.POST.get('event_description')
        date = request.POST.get('event_date')
        location = request.POST.get('event_location')
        if title and description and date and location:
            event.event_title = title
            event.event_description = description
            event.event_date = date
            event.event_location = location
            event.updated_on = timezone.now()
            event.save()
            return redirect('view_event', pk=pk)
        else:
            return HttpResponse("Please provide all required fields.")
    return render(request, 'update_event_form.html', {'event': event})

def rsvp_to_event(request, pk):
    event = get_object_or_404(EventDetail, pk=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = request.user
            if not AttendeeRecord.objects.filter(attendee_user=user, event_detail=event).exists():
                AttendeeRecord.objects.create(attendee_user=user, event_detail=event)
                return redirect('view_event', pk=pk)
            else:
                return HttpResponse("You are already RSVPed to this event.")
    else:
        return HttpResponse("You need to be logged in to RSVP.")
    return render(request, 'rsvp_event.html', {'event': event})

def send_event_reminder(event):
    subject = f"Reminder: {event.event_title}"
    message = f"Don't forget about the event '{event.event_title}' happening on {event.event_date}."
    from_email = 'your-email@example.com'
    recipient_list = [attendee.attendee_user.email for attendee in AttendeeRecord.objects.filter(event_detail=event)]
    try:
        send_mail(subject, message, from_email, recipient_list)
    except Exception as e:
        print(f"Error sending email: {e}")

def log_user_activity(request):
    if request.user.is_authenticated:
        UserActivityLog.objects.create(
            activity_user=request.user,
            activity_description=request.path
        )
def signup(request):
    first_name=''
    last_name=''
    email=''
    username=''
    password=''
    try:
        if request.method == 'POST':
            first_name = request.POST.get('first_name','')
            last_name = request.POST.get('last_name','')
            email = request.POST.get('email','')
            username = request.POST.get('username','')
            password = request.POST.get('password','')
            data=Signup_aten(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            data.save()
            
    except Exception as e:
        pass
    return render(request,'signup.html',{'first_name':first_name})
def login(request):
    username=''
    password=''
    ans={}

    try:
        if request.method=='POST':
            username=request.POST.get('username','')
            password=request.POST.get('password','')
            data=Signup.objects.all()
            for i in data:
                if i.username==username and i.password==password:
                    ans={'data': username }
                    return redirect('view_event')
                else:
                    ans={'data': 'wrong crediential'}
            

    except Exception as e:
        pass
    return render(request,'login.html',ans)
