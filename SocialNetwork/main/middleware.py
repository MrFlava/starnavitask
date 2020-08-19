from django.utils.timezone import now

from .models import  UserActivity


class SetLastVisitMiddleware(object):
    def process_response(self, request, response):
        if request.user.is_authenticated():
            UserActivity.objects.filter(user=request.user.pk).update(last_visit=now())
        return response
