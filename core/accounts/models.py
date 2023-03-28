from django.db import models
from django.db.models import TextChoices
from django.contrib.auth.models import AbstractUser


class Choice(TextChoices):
    MAN = 'Man', 'Мужчина'
    WOMAN = 'Woman', 'Женщина'


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name='Почта',
        unique=True,
        null=False,
        blank=False
    )
    avatar = models.ImageField(
        null=False,
        blank=False,
        upload_to='user_pic',
        verbose_name='Аватар'
    )
    birth_date = models.DateField(
       null=True,
       blank=True,
       verbose_name='Дата рождения'
    )
    gender = models.CharField(
        choices=Choice.choices,
        max_length=70,
        verbose_name='Пол'
    )
    phone = models.CharField(
        max_length=80,
        verbose_name='Телефон',
        null=True,
        blank=True,
        default=f'8-777-222-22-22'
    )
    info = models.CharField(
        max_length=200,
        verbose_name='Информация о пользователе',
        null=True,
        blank=True,
        default='Info'
    )
    commented_post = models.ManyToManyField(
        to='instagram.Post',
        verbose_name='Прокамментированные посты',
        related_name='user_comments'
    )
    laked_post = models.ManyToManyField(
        to='instagram.Post',
        verbose_name='Лайки поста',
        related_name='user_likes'
    )
    subscriptions = models.ManyToManyField(
        to='accounts.Account',
        verbose_name='Подписки',
        related_name='subscriptions_acc'
    )
