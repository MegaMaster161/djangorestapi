from django.db import models

#описываем модель статьи
class Article(models.Model):
    title = models.CharField()
    titleimg = models.CharField()
    meta = models.CharField()
    active = models.IntegerField()
    body = models.CharField()
    owner = models.IntegerField()
    createdAt = models.DateField()
    updateAt = models.DateField()

#описываем модель пользователя
class Users(models.Model):
    name = models.CharField()
    mail = models.CharField()
    hash_pass = models.CharField()
    active = models.IntegerField()
    role = models.CharField()
    createdAt = models.DateField()
    updateAt = models.DateField()

    