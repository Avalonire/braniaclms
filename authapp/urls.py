from authapp.apps import AuthappConfig
from django.urls import path
from authapp.views import LoginView, RegisterView, LogoutView, EditView

app_name = AuthappConfig

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('login/', RegisterView.as_view(), name='register'),
    path('login/', LogoutView.as_view(), name='logout'),
    path('login/', EditView.as_view(), name='edit '),

]
