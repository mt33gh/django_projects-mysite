from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'route'

urlpatterns = [
    path('', TemplateView.as_view(template_name='route/main.html'), name='home'),
    path('first', views.FirstView.as_view(), name='first-view'),
    path('second', views.SecondView.as_view(), name='second-view'),
]
