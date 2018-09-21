from django.db import models


class Post(models.Model):

    title = models.CharField(
        blank=False,
        max_length=100,
    )
    content = models.TextField(
        blank=False,
    )
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
