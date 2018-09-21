from django.urls import path
from cms.models import Post
from cms.views import PostListView, DraftListView, publish_post_view, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('drafts', DraftListView.as_view(), name="draft_list"),
    path('<int:pk>/publish', publish_post_view, name="publish_post"),
    path('new', PostCreateView.as_view(), name="post_form"),
]
