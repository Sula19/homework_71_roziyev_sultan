from django.db import models
from django.contrib.auth import get_user_model


class Comment(models.Model):
    author = models.ForeignKey(
        verbose_name='Автор',
        to=get_user_model(),
        related_name='author_comment',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        verbose_name='Публикация',
        to='instagram.Post',
        on_delete=models.CASCADE,
        default='Post',
        related_name='comment_post'
    )
    text = models.CharField(
        verbose_name='Комментарий',
        null=False,
        blank=False,
        max_length=200
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
        return f'{self.post} - {self.author} - {self.text}'
