from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('', views.slackUser_list),
    path('/redirect/', redirect_view)
]

urlpatterns = format_suffix_patterns(urlpatterns)