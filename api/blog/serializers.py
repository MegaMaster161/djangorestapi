from rest_framework import serializers
from blog.models import Article


class ArticleSerializer(serializers.Serializer):
    class Meta:
        model = Article
        fields = ('title', 'title', 'meta', 'slug', 'active', 'body', 'owner',) 
#        context = {'request': request}