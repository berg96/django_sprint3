from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class PublishedModel(models.Model):
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    
    class Meta:
        abstract = True


class CrearedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        abstract = True


class Location(PublishedModel, CrearedModel):
    name = models.CharField(max_length=256, verbose_name='Название')
    
    class Meta():
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Category(PublishedModel, CrearedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

class Post(PublishedModel, CrearedModel):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(verbose_name='Время публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
        )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title