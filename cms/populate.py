from django.http import HttpResponse

from .models import Post
from django.contrib.auth.models import Group

title1 = "POST - TITLE"
title2 = "PUBLISHED POST"
title3 = "DRAFT POST (UNPUBLISHED)"
content1 = "CONTENT CONTENT CONTENT BLA BLA BLA"


def populate(request):
    # Group.objects.all().delete()
    Post.objects.all().delete()

    Post.objects.create(title=title1, content=content1, published=True)
    Post.objects.create(title=title2, content=content1, published=True)
    Post.objects.create(title=title3, content=content1, published=False)

    Group.objects.create(name='author')
    Group.objects.create(name='editor')

    return HttpResponse("Database populated!")

