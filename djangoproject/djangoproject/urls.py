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
from rest_framework.urlpatterns import format_suffix_patterns

from api.views import SNTViewView, UserListView, UserDetailView
from test_app.views import index_page, WorkerView

#router = routers.DefaultRouter()
#router.register(r'api/users', UserListView.as_view(), basename='users')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("test", index_page),
    path("api/snt", SNTViewView.as_view()),
    path("api/users", UserListView.as_view()),
    path('api/users/<str:email>/<str:password>', UserDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
#urlpatterns += router.urls
