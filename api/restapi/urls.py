from django.urls import path

from blog.views import ArticleView

app_name = 'blog'

urlpatterns = [
    path('articles/', ArticleView.as_view()),
]