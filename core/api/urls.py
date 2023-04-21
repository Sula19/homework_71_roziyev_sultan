from django.urls import path, include
from rest_framework import routers
from .views import PostAPIView

router = routers.DefaultRouter()
router.register(r'post', PostAPIView)

urlpatterns = [
    path('auth/', include('rest_framework.urls'), name='rest_framework'),
    path('', include(router.urls)),
]
