from django.db import models
from blog.models import Article

from django.contrib.auth.models import User
# Create your models here.

class Comments(models.Model):
    """Модель для работы с комментариями пользователей"""
    author = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author')
    body = models.TextField()
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='article')
    createAt = models.DateTimeField(auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True)
   
    class Meta:
        ordering = ('-createAt',)


    def __str__(self):
        return self.body    
