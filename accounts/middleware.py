from django.utils import timezone

from accounts import models


class UpdateLastActivityMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            models.User.objects.filter(pk=request.user.id).update(
                last_activity=timezone.now()
            )

        return response
