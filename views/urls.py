from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='views'
urlpatterns = [
# pre-defined class from Django
    path('', TemplateView.as_view(template_name='views/main.html')),
# function from views.py
    path('funky', views.funky),

]

