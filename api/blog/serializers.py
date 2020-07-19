from rest_framework import serializers, request
from .models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.Serializer):
    """ Серилизируем выдачу данных. 
        В дальнешем для сериализации попробую использовать
        serializers.HyperlinkedModelSerializer. 
        Разобраться с пространством имён, т.к. 
        использую cвязь один о многим в поле owner. """
    id = serializers.CharField()
    title = serializers.CharField(max_length=250)
    titleimg = serializers.CharField(max_length=250)
    meta = serializers.CharField()
    slug = serializers.SlugField(max_length=250)
    active = serializers.CharField(max_length=15)
    body = serializers.CharField()
    owner = serializers.CharField()



