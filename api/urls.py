# from django.urls import include, path
# from rest_framework.routers import DefaultRouter
# from api.views import SlackUserViewSet

# router = DefaultRouter()
# router.register('api', SlackUserViewSet)

# urlpatterns = [
#     path('', include(router.urls))
# ]

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('', views.slackUser_list)
]

urlpatterns = format_suffix_patterns(urlpatterns)