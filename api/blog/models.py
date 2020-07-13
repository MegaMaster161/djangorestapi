from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#описываем модель статьи
class Article(models.Model):
    ACTIVE_CHOICES = (
        ('draft','Черновик'),
        ('pub', 'Опубликовано'),
    )
    title = models.CharField()
    titleimg = models.CharField()
    meta = models.CharField()
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

#описываем модель пользователя
class Users(models.Model):
    name = models.CharField()
    mail = models.CharField()
    hash_pass = models.CharField()
    active = models.IntegerField()
    role = models.CharField()
    createdAt = models.DateField()
    updateAt = models.DateField()

    