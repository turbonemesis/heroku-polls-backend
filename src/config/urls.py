from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='/login.html')),
    path('admin/', admin.site.urls),
    path("o/", include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/', include('polls.urls')),
]
