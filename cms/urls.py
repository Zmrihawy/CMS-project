from django.urls import path
from django.views.generic import ListView

from cms.models import Post

urlpatterns = [
    path('', ListView.as_view(model=Post), name="post_list"),
]
