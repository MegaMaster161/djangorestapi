from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Article
from blog.serializers import ArticleSerializer


class ArticleView(APIView):
    """Описываем модель для REST API"""
    def get(self, request):
        """Методом гет отдаём список статей REST API"""
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, context={'request': request}, many=True)
        return Response({"articles": serializer.data})
