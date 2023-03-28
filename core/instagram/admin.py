from django.contrib import admin
from instagram.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'description', 'image', 'created', 'updated')
    list_filter = ('id', 'author', 'created')
    search_fields = ('author',)
    fields = ('author', 'description', 'image', 'created', 'updated')
    readonly_fields = ('id', 'created', 'updated')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'post', 'created', 'updated')
    list_filter = ('id', 'author', 'created')
    search_fields = ('author', 'post')
    fields = ('author', 'text', 'post', 'created', 'updated')
    readonly_fields = ('id', 'created', 'updated')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
