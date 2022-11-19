from django.contrib.auth.views import LogoutView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView

from authapp.forms import CustomUserCreationForm, CustomUserChangeForm
from authapp.models import User


class CustomLoginView(TemplateView):
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

# class RegisterView(TemplateView):
#     template_name = 'authapp/User_form.html'
#     extra_context = {
#         'title': 'Регистрация пользователя'
#     }
#
#     def post(self, request, *args, **kwargs):
#         try:
#             if all(
#                     (
#                             request.POST.get('username'),
#                             request.POST.get('password1'),
#                             request.POST.get('password2'),
#                             request.POST.get('first_name'),
#                             request.POST.get('last_name'),
#                             request.POST.get('password1') == request.POST.get('password2'),
#                     )
#
#             ):
#                 new_user = User.objects.create(
#                     username=request.POST.get('username'),
#                     first_name=request.POST.get('first_name'),
#                     last_name=request.POST.get('last_name'),
#                     email=request.POST.get('email'),
#                     age=request.POST.get('age') if request.POST.get('age') else 0,
#                     avatar=request.FILES.get('avatar')
#                 )
#                 new_user.set_password(request.POST.get('password1'), )
#                 new_user.save()
#                 messages.add_message(request, messages.INFO, 'Регистрация успешно завершена!')
#                 return HttpResponseRedirect(reverse('authapp:login'))
#             else:
#                 messages.add_message(
#                     request,
#                     messages.WARNING,
#                     'Что-то пошло не так!'
#                 )
#                 return HttpResponseRedirect(reverse('authapp:register'))
#         except Exception:
#             messages.add_message(
#                 request,
#                 messages.WARNING,
#                 'Что-то пошло не так!'
#             )
#             return HttpResponseRedirect(reverse('authapp:register'))


# class EditView(TemplateView):
#     template_name = 'authapp/edit.html'
#
#     extra_context = {
#         'title': 'Изменение информации'
#     }
#
#     def post(self, request, *args, **kwargs):
#         if request.POST.get('username'):
#             request.user.username = request.POST.get('username')
#
#         if request.POST.get('first_name'):
#             request.user.first_name = request.POST.get('first_name')
#
#         if request.POST.get('last_name'):
#             request.user.last_name = request.POST.get('last_name')
#
#         if request.POST.get('age'):
#             request.user.age = request.POST.get('age')
#
#         if request.POST.get('email'):
#             request.user.email = request.POST.get('email')
#
#         request.user.save()
#         return HttpResponseRedirect(reverse('authapp:edit '))
