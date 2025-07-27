from django.urls import path
from .views import MainView
from . import views

app_name='views2'
urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('main2', views.MainView2.as_view()),
    path('restmain2/<slug:guess>', views.RestMainView2.as_view()),
# function from views.py
    path('funky', views.funky),
    path('danger', views.danger),
    path('game', views.game),
    path('game2', views.game2),
    path('game3', views.game3),
    path('rest/<int:guess>', views.rest),
    path('bounce', views.bounce),
]
