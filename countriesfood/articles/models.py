from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название блюда')
    content = models.TextField(blank=True, verbose_name='Описание блюда')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    country = models.ForeignKey('Country', on_delete=models.PROTECT, verbose_name='Страна')
    intro_picture = models.ImageField(upload_to='intro_pictures/%Y/%m/%d/', verbose_name='Обложка')
    pictures = models.ManyToManyField('Pictures', verbose_name='Изображения', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


class Country(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название страны')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
        ordering = ['title']


class Pictures(models.Model):
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', verbose_name='Изображения')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
