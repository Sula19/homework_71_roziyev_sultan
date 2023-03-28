from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    description = models.TextField(
        verbose_name='Описание',
        null=False,
        max_length=3000
    )
    image = models.ImageField(
        verbose_name='Картина',
        null=False,
        blank=True,
        upload_to='posts'
    )
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='author_post',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    created = models.DateTimeField(
        verbose_name='Дата и время создания',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Дата и время редактирования',
        auto_now=True
    )

    def __str__(self):
        return f'{self.author} - {self.description}'
