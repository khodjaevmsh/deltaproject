from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey(
        'blog.Post', on_delete=models.CASCADE, related_name='comments')
    author_name = models.CharField('Foydalanuvchi', max_length=50)
    comment_text = models.TextField('Kommentariya', max_length=1000)

    def __str__(self):
        return self.author_name or self.comment_text

    class Meta:
        verbose_name = 'Kommentariya'
        verbose_name_plural = 'Kommentariyalar'


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField()
    date = models.DateTimeField(default=timezone.now)
    popular = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Postral'

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})
