# Generated by Django 4.1.7 on 2023-03-24 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0012_remove_post_commented_post'),
        ('accounts', '0007_remove_account_commented_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='subscribers_count',
        ),
        migrations.RemoveField(
            model_name='account',
            name='subscriptions_count',
        ),
        migrations.AddField(
            model_name='account',
            name='commented_post',
            field=models.ManyToManyField(related_name='user_comments', to='instagram.comment', verbose_name='Прокамментированные посты'),
        ),
    ]