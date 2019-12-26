from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import redis


# Create your views here.

class KeyValueStoreView(APIView):
    def get(self, request, format=None):
        r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)

        should_update_ttl = True
        retrieved_keys = request.query_params.get('keys', '').split(',')
        keys = [val.strip() for val in retrieved_keys if val.strip()]
        if not keys:
            keys = r.keys()
            should_update_ttl = False

        values = {}
        for key in keys:
            if r.exists(key):
                values[key] = r.get(key)

                if should_update_ttl:
                    r.expire(key, settings.REDIS_TTL)

        return Response(values, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)

        if not request.data.items():
            return Response({'error': 'body can not be empty'}, status=status.HTTP_400_BAD_REQUEST)

        values = {}
        for key, value in request.data.items():
            if key and value and not r.exists(key):
                values[key] = value
                r.set(key, value, settings.REDIS_TTL)

        if values:
            return Response(values, status=status.HTTP_201_CREATED)

        return Response(values, status=status.HTTP_200_OK)

    def patch(self, request, format=None):
        r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True)

        if not request.data.items():
            return Response({'error': 'body can not be empty'}, status=status.HTTP_400_BAD_REQUEST)

        values = {}
        for key, value in request.data.items():
            if r.exists(key):
                values[key] = value
                r.set(key, value, settings.REDIS_TTL)

        return Response(values, status=status.HTTP_200_OK)
