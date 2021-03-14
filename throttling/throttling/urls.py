"""throttling URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from crudapi import views
from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken.views import obtain_auth_token

# create router object

router=DefaultRouter()
router.register('studentapi',views.StudentModelViewSet,basename='student')
# router.register('studentapi',views.StudentReadOnlyModelViewSet,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    # 1st way  is from admin panel
    # 2nd way is from drf_create_token function
    # 3rd way to create or get token
    # path('gottoken/',obtain_auth_token),
]
