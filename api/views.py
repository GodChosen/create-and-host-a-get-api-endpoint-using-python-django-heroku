from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import SlackUser
from api.serializers import SlackUserSerializer


@api_view(['GET'])
def slackUser_list(request, format=None):
    
    slackUser = SlackUser.objects.all()
    serializer = SlackUserSerializer(slackUser, many=True)
    return Response(serializer.data[0])

def redirect_view(request):
    response = redirect('/?format=json/')
    return response
