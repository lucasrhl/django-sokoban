"""sokobanProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from sokoban.views.index import IndexView
from sokoban.views.log import LoginView, LogoutView
from sokoban.views.map.list import MapListView
from sokoban.views.map.map import MapView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(),
         name='index'),
    path('login/', LoginView.as_view(),
         name='login'),
    path('logout/', LogoutView.as_view(),
         name='logout'),
    path('backoffice/', login_required(TemplateView.as_view(template_name='map_list_view.html')),
         name="back_log"),
    path('map/list/', MapListView.as_view(),
         name='map_list'),
    path('map/<int:pk>', MapView.as_view(),
         name='map'),
]
