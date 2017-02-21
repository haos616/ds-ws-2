from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from core.tasks import hello


class TimeAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, format=None):
        now = timezone.now()
        hello.delay()
        return Response(now)
