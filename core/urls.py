from django.urls import path
from .views import RegisterUserView, UserGetUpdateView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile', UserGetUpdateView.as_view(), name='profile')
]
