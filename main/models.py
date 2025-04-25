from django.db import models
from django.contrib.auth.models import User

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=200, verbose_name='Тема')
    message = models.TextField(verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['-created_at']

class Article(models.Model):
    title = models.CharField('Название', max_length=200)
    content = models.TextField('Содержание')
    image = models.ImageField('Изображение', upload_to='articles/', null=True, blank=True)
    short_description = models.TextField('Краткое описание', max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField('Опубликовано', default=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Автор')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']

class Comment(models.Model):
    text = models.TextField(verbose_name='Текст комментария')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата комментария')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments', verbose_name='Статья')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-date']

    def __str__(self):
        return f'Комментарий от {self.author.username} к {self.article.title}'
