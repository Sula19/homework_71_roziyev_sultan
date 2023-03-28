from django.urls import path

from instagram.views.views import (IndexView,
                                   CreatePost,
                                   AddLike,
                                   Subscribes,
                                   AddComment,
                                   UpdatePost,
                                   DeletePost,
                                   DetailPost,
                                   UpdateComment,
                                   DeleteComment,
                                   CommentList)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_post', CreatePost.as_view(), name='add_post'),
    path('detail_post/<int:pk>', DetailPost.as_view(), name='detail_post'),
    path('update_post/<int:pk>', UpdatePost.as_view(), name='update_post'),
    path('delete_post/<int:pk>', DeletePost.as_view(), name='delete_post'),
    path('update_comment/<int:pk>', UpdateComment.as_view(), name='update_comment'),
    path('delete_comment/<int:pk>', DeleteComment.as_view(), name='delete_comment'),
    path('comments', CommentList.as_view(), name='comments'),
    path('post/<int:pk>', AddLike.as_view(), name='likes'),
    path('user/<int:pk>', Subscribes.as_view(), name='sub'),
    path('post/<int:pk>/commented', AddComment.as_view(), name='commented')
]
