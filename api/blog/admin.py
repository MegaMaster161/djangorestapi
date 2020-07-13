from django.contrib import admin
from .models import Article

# Фиксируем модель статьи
admin.site.register(Article)
