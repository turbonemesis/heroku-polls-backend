from django.urls import include, path
from rest_framework.routers import SimpleRouter
from django.conf.urls import include, url

from .twilio.views import TwilioHandler
from . import views

__app_name__ = 'polls'

router = SimpleRouter()
router.register('polls', views.QuestionViewSet)
# router.register('createTask', TwilioHandler.as_view())

urlpatterns = [
    url(r'^createTask$', TwilioHandler.as_view()),
    path('v1/', include(router.urls)),
]
