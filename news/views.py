from django.shortcuts import render, get_object_or_404, redirect
from .models import News

# Create your views here.
def news_list(request):
    news = News.objects.all().order_by('-created_at')
    context = {'news': news}
    return render(request, 'news_list.html', context) 

def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    news.views_count += 1
    news.save( update_fields=['views_count'] )
    context = {'news' : news}
    return render(request, 'news_detail.html', context )

