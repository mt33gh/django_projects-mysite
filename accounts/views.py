from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.auth.models import User

class IndexView(generic.ListView):
    model = User
    template_name = "accounts/index.html"
