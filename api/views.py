# from django.shortcuts import render
# from api.models import SlackUser
# from rest_framework import viewsets
# from .serializers import SlackUserSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import SlackUser
from api.serializers import SlackUserSerializer


@api_view(['GET'])
def slackUser_list(request, format=None):
    
    slackUser = SlackUser.objects.all()
    serializer = SlackUserSerializer(slackUser, many=True)
    return Response(serializer.data)
# from rest_framework.generics import RetrieveAPIView

# Create your views here.
# class SlackUserViewSet(viewsets.ModelViewSet):
#     # API endpoint that allows users to be viewed or edited.
    
#     queryset = SlackUser.objects.all()
#     serializer_class = SlackUserSerializer
    
# class GetSlackUser(RetrieveAPIView):
#     serializer_class = SlackUserSerializer
#     objectset = SlackUser.objects.all()

