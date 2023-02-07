from django.views.generic.base import TemplateView

from common.views import TitleMixin


class HomeView(TitleMixin, TemplateView):
    template_name = 'generator/home.html'
    title = 'SPG | Simple Password Generator'
