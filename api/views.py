from django.shortcuts import render
from djoser.serializers import UserSerializer, UserCreateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .tasks import notify_customers


@api_view(['GET'])
@permission_classes([AllowAny])
def ping_pong(request):
    notify_customers('fak')
    notify_customers.delay('hello mothertruckers!')
    return Response('pong!', status=status.HTTP_200_OK)