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

from api.views import UserListView, UserDetailView
from docs.views import DocDetailView, DocListView
from meetings.views import MeetingListView, MeetingDetailView
from snts.views import SNTView
from test_app.views import index_page

#router = routers.DefaultRouter()
#router.register(r'api/users', UserListView.as_view(), basename='users')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("test", index_page),

    path('api/snt', SNTView.as_view()),
    path('api/snt/', SNTView.as_view()),

    path('api/users', UserListView.as_view()),
    path('api/users/<str:email>/', UserDetailView.as_view()),

    path('api/meetings', MeetingListView.as_view()),
    path('api/meetings/<int:id>/', MeetingDetailView.as_view()),

    path('api/docs', DocListView.as_view()),
    path('api/docs/<int:id>/', DocDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
#urlpatterns += router.urls
