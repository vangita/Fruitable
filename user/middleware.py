from django.utils import timezone
from .models import User

class UpdateLastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'user_id' in request.session:
            user = User.objects.get(id=request.session['user_id'])
            user.last_active_datetime = timezone.now()
            user.save()
        response = self.get_response(request)
        return response
