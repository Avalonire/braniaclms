from django.shortcuts import render
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from authapp.forms import CustomUserCreationForm, CustomUserChangeForm
from authapp.models import User


class CustomLoginView(LoginView):
    template_name = 'authapp/login.html'
    extra_context = {
        'title': 'Вход пользователя'
    }


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('mainapp:index')


class EditView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    template_name = 'authapp/edit.html'

    # Контроллер сразу для получения только текущего пользователя, без показа id
    def get_object(self, queryset=None):
        return self.request.user

    # Передаем url пользователя сразу, с его id
    def get_success_url(self):
        return reverse_lazy('authapp:edit', args=[self.request.user.pk])


class CustomLogoutView(LogoutView):
    pass
