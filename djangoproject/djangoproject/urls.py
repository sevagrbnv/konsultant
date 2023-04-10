from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users.views import UserListView, UserDetailView
from docs.views import DocDetailView, DocListView, FileUploadView, FileDownloadView, ZipDownloadView, DocCreateView
from meetings.views import MeetingListView, MeetingDetailView
from questions.views import QuestionListView, QuestionDetailView
from snts.views import SNTView, ALL
from votes.views import VoteDetailView, VoteListView

#router = routers.DefaultRouter()
#router.register(r'users/users', UserListView.as_view(), basename='users')

urlpatterns = [
    path("admin/", admin.site.urls),

    path('api/snt', SNTView.as_view()),
    path('api/snt/', SNTView.as_view()),

    path('api/users', UserListView.as_view()),
    path('api/users/<str:email>/', UserDetailView.as_view()),

    path('api/meetings', MeetingListView.as_view()),
    path('api/meetings/<int:id>/', MeetingDetailView.as_view()),

    path('api/docs', DocListView.as_view()),
    path('api/docs/<int:id>/', DocDetailView.as_view()),

    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('create', DocCreateView.as_view(), name='file-create'),
    # @deprecated
    path('download/<int:pk>/', FileDownloadView.as_view(), name='file-download'),
    path('docs/download/<int:meeting_id>/', ZipDownloadView.as_view(), name='zip-download'),

    path('api/quests', QuestionListView.as_view()),
    path('api/quests/<int:id>/', QuestionDetailView.as_view()),

    path('api/votes', VoteListView.as_view()),
    path('api/votes/<int:id>/', VoteDetailView.as_view()),

    path('api/all', ALL.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
#urlpatterns += router.urls
