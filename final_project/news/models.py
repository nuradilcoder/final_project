from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    views_count = models.IntegerField(default=0 ,verbose_name='Просмотры')
    news_image = models.ImageField(upload_to='news_image/',blank=True,null=True,verbose_name='Новостное изображение')
    
    def __str__(self):
        return self.title
    
    

    