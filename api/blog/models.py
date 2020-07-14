from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#описываем модель статьи
class Article(models.Model):
    ACTIVE_CHOICES = (
        ('draft','Черновик'),
        ('pub', 'Опубликовано'),
    )
    title = models.CharField(max_length=250)
    titleimg = models.CharField(max_length=250,)
    meta = models.TextField()
    slug = models.SlugField(max_length=250,unique_for_date='createdAt')
    active = models.CharField(max_length=15, choices=ACTIVE_CHOICES, default='draft')
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, 
                                blank=True, null=True, related_name='blog_posts')
    createdAt = models.DateField()
    updateAt = models.DateField()

    
    class Meta:
        ordering = ('-createdAt',)


    def __str__(self):
        return self.title


    