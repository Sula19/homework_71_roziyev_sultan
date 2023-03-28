from django.urls import path
from accounts.views import (RegisterView,
                            ProfileView,
                            LoginView,
                            logout_view,
                            UserChangeView,
                            UserPasswordChange,
                            Subscriptions,
                            Subscribers)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('user_change/<int:pk>', UserChangeView.as_view(), name='change'),
    path('user/password_change/<int:pk>', UserPasswordChange.as_view(), name='password_change'),
    path('<int:pk>/subscriptions', Subscriptions.as_view(), name='subscriptions'),
    path('<int:pk>/subscribers', Subscribers.as_view(), name='subscribers')

]
