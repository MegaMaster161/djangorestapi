from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateAPIView,)
from django.http import Http404
from django.shortcuts import get_object_or_404
from blog.models import Article
from blog.serializers import ArticleSerializer
from rest_framework import status
from .modules import slugify, change_value_in_dict
from rest_framework.permissions import IsAuthenticated


class ArticleView(APIView):
    """Описываем модель для REST API"""
    def get(self, request):
        """Методом гет отдаём весь список статей REST API"""
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, context={'request': request}, many=True)
        return Response({"articles": serializer.data})


class GetOrUpdateOneArticle(RetrieveUpdateAPIView):
    """Описываем получение/изменении одной статьи по PK"""

    def get(self, request, pk):
        """Метод для получения данных о статье"""
        article = get_object_or_404(Article, id=pk)
        serializer = ArticleSerializer(article)
        return Response({"article": serializer.data})

    def put(self, request, pk):
        """Метод для обновления содержимого статьи"""
        article = get_object_or_404(Article, id=pk)
        serializer = ArticleSerializer(article, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticlePost(ListCreateAPIView):
    permission_classes = [IsAuthenticated,]

    def post(self, request):
        """Создаём пост"""
        request_data = request.data.copy()
        change_data = {"owner": request.user.id, "slug": slugify(request.data["title"])}
        change_value_in_dict(change_data, request_data)
        serializer = ArticleSerializer(data=request_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
