from django.shortcuts import render, get_object_or_404, redirect
from .models import News

# Create your views here.
def news_list(request):
    news = News.objects.all().order_by('-created_at')
    theme = request.GET.get('theme', '1')
    if theme == '1':
        theme_text = 'dark-theme'
        theme = 0
        png = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABPElEQVQ4T6WTvU4CURCFv7v+IIXrqrHQ2k4bRaIFPU9B688jaK+PYDSWxIewpyAB7YyF9hZmcYGCKMo4l4i5wu6K4XZ75+yZc2bONaQcuWfWls0G70kwk0bwWqNk64t5ymMRvFSYXynQHoDjCIYxPwrCKv7UNDfGUFrI8SSPZNpttkUQf447a6N5y7p+lz8/KC7v0erbc6VZQA8KCspq4dSq/643jHAiHm8eVGyDwX8jM2jUOdLL8zjPSnIY5Ll0a78IrOyoybPTeZgnDLKsuVsxUmcmEp22R88THtRCNW0zitlVzKbFB8L15ARuNxucqNO3sJSgIgxg1ezQTRxiVONADBexQzTsBzmuEoc4WKPpkVGSM0dJqPk4FugmrnEkSGqn1WHLdvPRIKnsP4M0UZTjPP/7MQ2TjPOcvwBMYo+xs0V5BAAAAABJRU5ErkJggg=="
    else:
        theme_text = 'light-theme'
        theme = 1
        png = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAABOklEQVQ4T5WTz0pCQRTGvQqFUStxl+C2rEX0BBGu6i2K7M+ihb6GmCAaPUiREL1CBEHLAnuBWliLyt8Xc+Pc67mIAz+Y883MN+fMnyg33TaRDmEXqvANLzCEC3izSyITLNLvQAPyKd9P4iZcwo9noMU3sONkNEbbg3tnLBdnMGDw2JuAdhJ2tsMVgl8YyUA1Pzhpa4H07VTaWnwVDI5koIM5z9j9FF3Z2bYaDHQWDRk8wXqGwRr6M/ynHOYlSvhAXM4wKKKXbcqq285VBu+wkmGwhF6yKdOfegfzlpAoZ9YhnrFj32SXuAGVI4MN0HUVnDIe0bYgfn2JG1A58UPqEWg3r3lZ/D0iTY4NFuhfgz5Quukf7MOd524/k0zaoKebLucLrRXOw/1M1rxGcAB1qIK+8yvcQld128kTiPZISM1cuicAAAAASUVORK5CYII="
    context = {'news': news, 'theme': theme_text, 'theme_var': theme, 'png': png }
    return render(request, 'news_list.html', context) 

def news_detail(request, id):
    news = get_object_or_404(News, id=id)
    news.views_count += 1
    news.save( update_fields=['views_count'] )
    theme = request.POST.get('theme', '1')
    if theme == '0':
        theme_text = 'dark-theme'
        theme = 1        
    else:
        theme_text = 'light-theme'
        theme = 0
    context = {'news' : news, 'theme': theme_text, 'theme_var': theme}
    return render(request, 'news_detail.html', context )

