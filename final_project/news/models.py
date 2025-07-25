from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title