from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Categroy(models.Model):
    '''分类'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    '''标签'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    '''文章'''
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Categroy)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    views = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']  # 指定文章排序方式
