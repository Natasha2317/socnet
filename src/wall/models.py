from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from src.comments.models import AbstractComment


class Post(models.Model):
    """ Post model
    """

    title = models.CharField('Заголовок поста', max_length=200, blank=True, null=True)
    text = models.TextField(max_length=3000)
    create_date = models.DateTimeField('Дата публикации',auto_now_add=True)
    published = models.BooleanField('Опубликовано',default=True)
    moderation = models.BooleanField(default=True)
    view_count = models.PositiveIntegerField('Количество просмотров',default=0)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts'
    )
    idtechnology = models.ManyToManyField('IdTechnology', max_length=100, null=True)

    def __str__(self):
        # Post by {self.user} -
        return self.title

    def comments_count(self):
        return self.comments.count()

    class Meta:
            ordering = ['create_date']

class IdTechnology(models.Model):
    """ IdTechnology model
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Comment(AbstractComment, MPTTModel):
    """ Модель коментариев к постам
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    parent = TreeForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children'
    )

    def __str__(self):
        return "{} - {}".format(self.user, self.post)
