# Generated by Django 4.1.7 on 2023-03-24 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0010_remove_post_comments_count_post_commented_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='commented_post',
            field=models.ManyToManyField(related_name='user_comments', to='instagram.comment', verbose_name='Прокамментированные посты'),
        ),
    ]