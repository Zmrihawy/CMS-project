from django.urls import path
from django.views.generic import ListView

from cms.models import Post
from cms.views import PostListView, DraftListView

urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('drafts', DraftListView.as_view(), name="draft_list"),
]
