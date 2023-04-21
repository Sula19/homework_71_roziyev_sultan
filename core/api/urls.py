from django.urls import path, include
from rest_framework import routers
from .views import PostAPIView, LikeAPIView

router = routers.DefaultRouter()
router.register(r'post', PostAPIView)
router.register(r'like', LikeAPIView)


urlpatterns = [
    path('auth/', include('rest_framework.urls'), name='rest_framework'),
    path('', include(router.urls)),
]
