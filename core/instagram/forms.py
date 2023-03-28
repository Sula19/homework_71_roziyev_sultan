from django import forms
from instagram.models import Post, Comment


class PostForm(forms.ModelForm):
    image = forms.ImageField(required=True, label='Картина')

    class Meta:
        model = Post
        fields = ('image', 'description')
        labels = {
            'image': 'Картина',
            'description': 'Описание',
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text': 'Комментарий',

        }
