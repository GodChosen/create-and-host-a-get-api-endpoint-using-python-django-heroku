from django.shortcuts import render
from api.models import SlackUsers
from rest_framework import viewsets
from .serializers import SlackUsersSerializer

# Create your views here.
# class SlackUsersViewSet(viewsets.ModelViewSet):
#     # API endpoint that allows users to be viewed or edited.
    
#     queryset = SlackUsers.objects.all().order_by('-slackUsername')
#     serializer_class = SlackUsersSerializer
    
class GetSlackUsers(RetrieveAPIView):
    queryset = SlackUsers.objects.all().order_by('-slackUsername')
    serializer_class = SlackUsersSerializer

