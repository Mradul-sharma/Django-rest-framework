# crypto_app/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .tasks import fetch_crypto_data
from celery.result import AsyncResult

class StartScrapingView(APIView):
    def post(self, request, *args, **kwargs):
        coins = request.data.get('coins', [])
        task = fetch_crypto_data.apply_async((coins,))
        return Response({'job_id': task.id}, status=status.HTTP_202_ACCEPTED)

class ScrapingStatusView(APIView):
    def get(self, request, job_id, *args, **kwargs):
        result = AsyncResult(job_id)
        if result.state == 'PENDING':
            return Response({'status': 'Pending'}, status=status.HTTP_200_OK)
        elif result.state != 'FAILURE':
            return Response({'job_id': job_id, 'result': result.result}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'Failure'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
