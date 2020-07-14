from django.contrib import admin
from .models import Article

# через конструкцию декоратора определяем 
# отображаемые поля для модели статей
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'owner', 'createdAt', 'active')
    list_filter = ('active', 'owner', 'createdAt')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('owner',)
    date_hierarchy = 'createdAt'
    ordering = ('active', 'createdAt')
