"""player URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app import views
from player import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('admin', admin.site.urls),
    path('login', views.login),
    path('logout', views.logout),
    path('my', views.personal_info),
    path('log', views.log_info),
    path('list', views.video_list),
    path('q_all', views.query_all),
    path('list/get', views.get_video_list),
    path('video/detail', views.play_video),
    path('video/hash', views.hash_verity),
    path('video/download',views.download_from_ftp)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
