from django.urls import include, path
from rest_framework.routers import SimpleRouter
from django.conf.urls import include, url
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views

from .twilio.views import TwilioHandler
from . import views

__app_name__ = 'polls'

router = SimpleRouter()
router.register('polls', views.QuestionViewSet)
# router.register('createTask', TwilioHandler.as_view())

urlpatterns = [
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='/login.html')),
    # path("admin", admin.site.urls),

    url(r'^createTask$', TwilioHandler.as_view()),
    path('v1/', include(router.urls)),
]
