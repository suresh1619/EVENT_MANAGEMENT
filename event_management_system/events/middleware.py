from .models import UserActivityLog

class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            UserActivityLog.objects.create(
                activity_user=request.user,
                activity_description=request.path
            )
        return response
