from django.db import models

# Create your models here.
class SlackUsers(models.Model):
    slackUsername = models.CharField(max_length= 15)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.CharField(max_length= 600)
    
    def __str__(self):
        return self.slackUsername
    