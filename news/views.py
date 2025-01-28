from django.shortcuts import render, redirect, get_object_or_404
from .models import New


def home(request):
    news = New.objects.all()
    ctx = {'news': news}
    return render(request, 'index.html', ctx)


def news_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        short_content = request.POST.get('short_content')
        long_content = request.POST.get('long_content')
        author = request.POST.get('author')
        category = request.POST.get('category')
        if title and short_content and long_content and author and category:
            New.objects.create(
                title=title,
                short_content=short_content,
                long_content=long_content,
                author=author,
                category=category
            )
            return redirect('home')
    return render(request, 'news/add-news.html')


def news_detail(request, news_id):
    news = get_object_or_404(New, pk=news_id)
    ctx = {'news': news}
    return render(request, 'news/detail.html', ctx)


def news_category(request, category):
    news = New.objects.filter(category=category)
    ctx = {'news': news, 'category': category}
    return render(request, 'news/news-by-category.html', ctx)
