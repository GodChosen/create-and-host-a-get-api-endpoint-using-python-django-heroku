from api.models import SlackUsers
from rest_framework import serializers

class SlackUsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SlackUsers
        fields = ["slackUsername", "backend", "age", "bio"]