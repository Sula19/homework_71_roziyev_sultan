# Generated by Django 4.1.7 on 2023-03-23 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_comment_author_comment_post_post_author'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='commented_post',
            field=models.ManyToManyField(related_name='user_comments', to='instagram.post', verbose_name='Прокамментированные посты'),
        ),
        migrations.AddField(
            model_name='account',
            name='laked_post',
            field=models.ManyToManyField(related_name='user_likes', to='instagram.post', verbose_name='Лайки поста'),
        ),
        migrations.AddField(
            model_name='account',
            name='subscriptions',
            field=models.ManyToManyField(related_name='subscribes', to='instagram.post', verbose_name='Подписки'),
        ),
    ]
