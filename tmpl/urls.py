from django.urls import path
from . import views

app_name='tmpl'
urlpatterns = [
    path("", views.index, name="index"),
    path("game/<slug:guess>", views.GameView.as_view()),
    path("game2/<slug:guess>", views.GameView2.as_view()),
    path("simple", views.simple, name="simple"),
    path("guess", views.guess, name="guess"),
    path("special", views.special, name="special"),
    path("loop", views.loop, name="loop"),
    path("nested", views.nested, name="nested"),
]
