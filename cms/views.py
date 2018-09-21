from django.views.generic import ListView
from django.views.generic.edit import CreateView
from cms.models import Post


class PostListView(ListView):
    context_object_name = 'posts'
    queryset = Post.objects.filter(published=True)


class DraftListView(PostListView):
    queryset = Post.objects.filter(published=False)
    template_name = 'post_list'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', ]
    success_url = '/drafts'
