from django.urls import path
from django.views.generic import DetailView

from cms.models import Post
from cms.populate import populate
from cms.views import PostListView, DraftListView, publish_post_view, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('drafts', DraftListView.as_view(), name="draft_list"),
    path('<int:pk>/publish', publish_post_view, name="publish_post"),
    path('new', PostCreateView.as_view(), name="post_form"),
    path('<int:pk>', DetailView.as_view(model=Post), name="post_detail"),


    path('populate', populate, name="populate"),
]
