from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from cms.models import Post


class PostListView(ListView):
    context_object_name = 'posts'
    queryset = Post.objects.filter(published=True)


class DraftListView(PostListView):
    queryset = Post.objects.filter(published=False)
    template_name = 'cms/post_list.html'
    
    
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', ]
    success_url = '/drafts'


class PostUpdateView(UpdateView):
    model = Post
    fields = PostCreateView.fields
    success_url = '/drafts'


########################################################
########################################################

def publish_post_view(request, pk):
    if request.method == 'POST':
        if request.user.groups.filter(name='editor').exists():
            post = Post.objects.get(pk=pk)
            post.published = True
            post.save()
            return HttpResponseRedirect(reverse_lazy("post_list"))
        return HttpResponse("You do not have permission to publish")
