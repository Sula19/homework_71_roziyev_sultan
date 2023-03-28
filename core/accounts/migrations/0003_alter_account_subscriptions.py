# Generated by Django 4.1.7 on 2023-03-23 06:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_commented_post_account_laked_post_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='subscriptions',
            field=models.ManyToManyField(related_name='subscribes', to=settings.AUTH_USER_MODEL, verbose_name='Подписки'),
        ),
    ]
