from django.urls import path
from cms.views import PostListView, DraftListView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('drafts', DraftListView.as_view(), name="draft_list"),
    path('new', PostCreateView.as_view(), name="post_form"),
]
