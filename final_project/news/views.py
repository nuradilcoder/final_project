from django.shortcuts import render, get_object_or_404, redirect
from .models import News

# Create your views here.
def news_list(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'news_list.html', context) 

def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    context = {'news' : news}
    return render(request, 'news_detail.html', context )