from django.views.generic.base import TemplateView

from common.views import TitleMixin
from generator.password_generator import random_generator


class HomeView(TitleMixin, TemplateView):
    template_name = 'generator/home.html'
    title = 'SPG | Simple Password Generator'


class PasswordView(TitleMixin, TemplateView):
    template_name = 'generator/password.html'
    title = 'SPG | You password'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['password'] = random_generator(request_data=self.request.GET)
        return context


class AboutView(TitleMixin, TemplateView):
    template_name = 'generator/about.html'
    title = 'SPG | About'
