from django.shortcuts import render
from api.models import SlackUser
from rest_framework import viewsets
from .serializers import SlackUserSerializer
# from rest_framework.generics import RetrieveAPIView

# Create your views here.
class SlackUserViewSet(viewsets.ModelViewSet):
    # API endpoint that allows users to be viewed or edited.
    
    queryset = SlackUser.objects.all().order_by('-id')
    serializer_class = SlackUserSerializer
    
# class GetSlackUser(RetrieveAPIView):
#     queryset = SlackUser.objects.all().order_by('-slackUsername')
#     serializer_class = SlackUserSerializer

