"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from sec.views import UserRegisterApiView, MatchAPI
from photos.views import ImageView
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/register/', UserRegisterApiView.as_view(), name='users_register'),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('photos/', ImageView.as_view(), name='photos-api'),
    path('match/', MatchAPI.as_view(), name='match-api')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)