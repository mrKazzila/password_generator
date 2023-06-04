from django.urls import path

from app.generator import views

urlpatterns = [
    path('', views.home_view, name='home'),
]
