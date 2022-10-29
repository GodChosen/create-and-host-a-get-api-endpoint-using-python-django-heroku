from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import SlackUser
from api.serializers import SlackUserSerializer
from django.http import JsonResponse
import json



@api_view(['GET'])
def slackUser_list(request, format=None):
    
    slackUser = SlackUser.objects.all()
    serializer = SlackUserSerializer(slackUser, many=True)
    return Response(serializer.data[0])


