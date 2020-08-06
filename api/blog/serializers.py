from rest_framework import serializers, request
from .models import Article
from django.contrib.auth.models import User



class ArticleSerializer(serializers.ModelSerializer):
    """ Серилизируем выдачу данных. 
        В дальнешем для сериализации попробую использовать
        serializers.HyperlinkedModelSerializer. 
        Разобраться с пространством имён, т.к. 
        использую cвязь один о многим в поле owner. """

    
    class Meta:
        model=Article
        fields='__all__'
