from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response


class TimeAPIView(APIView):
    def get(self, request, format=None):
        now = timezone.now()
        return Response(now)
