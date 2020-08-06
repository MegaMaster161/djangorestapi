from django.urls import path

from blog.views import (ArticleView, ArticlePost, GetOrUpdateOneArticle)

app_name = 'blog'

urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/create/', ArticlePost.as_view()),
    path('article/<int:pk>/', GetOrUpdateOneArticle.as_view()),
]