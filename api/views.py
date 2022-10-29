from django.shortcuts import render
from api.models import SlackUser
from rest_framework import viewsets
from .serializers import SlackUserSerializer
# from rest_framework.generics import RetrieveAPIView

# Create your views here.
# class SlackUserViewSet(viewsets.ModelViewSet):
#     # API endpoint that allows users to be viewed or edited.
    
#     queryset = SlackUser.objects.all()
#     serializer_class = SlackUserSerializer
    
class GetSlackUser(RetrieveAPIView):
    serializer_class = SlackUserSerializer
    objectset = SlackUser.objects.all()

