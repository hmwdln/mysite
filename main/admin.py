from django.contrib import admin
from .models import ContactMessage, Article, Comment

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published')
    list_filter = ('is_published', 'created_at', 'author')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    list_editable = ('is_published',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'article', 'date', 'text_preview')
    list_filter = ('date', 'author')
    search_fields = ('text', 'author__username', 'article__title')
    date_hierarchy = 'date'

    def text_preview(self, obj):
        return obj.text[:100] + '...' if len(obj.text) > 100 else obj.text
    text_preview.short_description = 'Текст комментария'
