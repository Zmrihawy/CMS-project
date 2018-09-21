from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView

from cms.models import Post


class PostListView(ListView):
    context_object_name = 'posts'
    queryset = Post.objects.filter(published=True)


class DraftListView(PostListView):
    queryset = Post.objects.filter(published=False)
    template_name = 'cms/post_list.html'


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

