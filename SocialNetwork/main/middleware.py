import datetime

from .models import UserActivity
from django.contrib.auth.models import User


class ActivityMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:

            user = User.objects.get(id=request.user.id)
            UserActivity.objects.filter(user_id=user).update(last_visit=datetime.datetime.now(), last_request=datetime.datetime.now())

        response = self.get_response(request)

        return response



