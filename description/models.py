from django.db import models

class Position(models.Model):
    name = models.CharField('Позиция', max_length=50)

    def __str__(self):
        return(self.name)

class Attribute(models.Model):
    name = models.CharField('Атрибут', max_length=50)

    def __str__(self):
        return self.name

class Hero(models.Model):
    name = models.CharField('Имя героя', max_length=100)
    slug = models.SlugField('Адрес страницы', unique=True)
    image = models.CharField('Путь к изображению', max_length=255)
    short_description = models.TextField('Краткое описание')
    description = models.TextField('Полное описание')
    is_published = models.BooleanField('Опубликован', default=True)
    is_on_main = models.BooleanField('На главной', default=False)
    positions = models.ManyToManyField(
        Position,
        verbose_name='Позиции',
        blank=True,
    )   
    attribute = models.ForeignKey(
        Attribute,
        on_delete=models.PROTECT,
        verbose_name='Атрибут',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name