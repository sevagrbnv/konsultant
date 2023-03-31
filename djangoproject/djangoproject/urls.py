"""djangoproject URL Configuration

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
from django.urls import path
from rest_framework.routers import SimpleRouter

from login.views import UserView, SntView
from test_app.views import index_page, WorkerView

router = SimpleRouter()

router.register('api/workers', WorkerView, basename='Worker')
router.register('api/snt', SntView, basename='SNT')
router.register('api/users', UserView, basename='Users')
#router.register('api/users/login', UserView.as_view({'post': 'login'}), basename='login')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_page),
]

urlpatterns += router.urls