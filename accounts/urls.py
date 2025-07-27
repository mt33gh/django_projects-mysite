from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "accounts"

# You can use either path.  Both works.
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"), 
    #path('', TemplateView.as_view(template_name='accounts/main.html')),
]
