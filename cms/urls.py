from django.urls import path
from django.views.generic import ListView

urlpatterns = [
    path('/', ListView.as_view(model=Post), name="post_view"),
]