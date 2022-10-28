from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import SlackUserViewSet

router = DefaultRouter()
router.register('api', SlackUserViewSet)

urlpatterns = [
    path('', include(router.urls))
]