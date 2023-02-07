import random

from django.views.generic.base import TemplateView

from common.views import TitleMixin


class HomeView(TitleMixin, TemplateView):
    template_name = 'generator/home.html'
    title = 'SPG | Simple Password Generator'


class PasswordView(TitleMixin, TemplateView):
    template_name = 'generator/password.html'
    title = 'SPG | You password'

    def random_generator(self):
        base_characters = list('abcdefghijklmnopqrstuvwxyz')
        data = self.request.GET

        length = int(data.get('length'))
        if data.get('uppercase'):
            base_characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        if data.get('numbers'):
            base_characters.extend(list('1234567890'))
        if data.get('special'):
            base_characters.extend(list('!@#$%^&*()-_=+'))

        password = ''
        for _ in range(length):
            password += random.choice(base_characters)

        return password

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['password'] = self.random_generator()
        return context
