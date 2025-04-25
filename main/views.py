from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import ContactMessage, Article, Comment
from .forms import UserRegisterForm, UserLoginForm, CommentForm, ArticleForm
from django.utils import timezone

def home(request):
    articles = Article.objects.filter(is_published=True).order_by('-created_at')[:3]
    return render(request, 'main/home.html', {'articles': articles})

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def contacts(request):
    message_sent = False
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        message_sent = True
        
    return render(request, 'main/contacts.html', {'message_sent': message_sent})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна!')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка входа')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'Вы вышли из системы')
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'main/profile.html')

def article_list(request):
    articles = Article.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'main/article_list.html', {'articles': articles})

def articles(request):
    articles = Article.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'main/articles.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id, is_published=True)
    comments = Comment.objects.filter(article=article)
    
    if request.method == "POST" and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            messages.success(request, 'Комментарий успешно добавлен!')
            return redirect('article_detail', article_id=article.id)
    else:
        form = CommentForm()
    
    return render(request, 'main/article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form,
    })

@login_required
@user_passes_test(lambda u: u.is_superuser)
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'main/article_create.html', {'form': form})

@login_required
def videopost(request):
    return render(request, 'main/video.html')
