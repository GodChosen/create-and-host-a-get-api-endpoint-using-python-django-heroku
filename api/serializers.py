from api.models import SlackUser
from rest_framework_json_api import serializers

class SlackUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlackUser
        fields = ["slackUsername", "backend", "age", "bio"]