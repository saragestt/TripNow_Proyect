from Users.views import UserView, LoginView
from django.urls import path

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('login/', LoginView.as_view(), name='login'),
]