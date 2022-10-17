from django.db import models
from accounts.models import User


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    text = models.TextField(blank=True)
    date_created = models.DateTimeField('Дата створення', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.FileField(upload_to='post-images/', blank=True)


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)