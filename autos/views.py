from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.models import Auto, Make

# Create your views here.
# This file is modified from the original views.py
# I deleted unnecessary lines of the code:
#     from django.shortcuts import render, redirect, get_object_or_404
#     from autos.forms import MakeForm

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.count()
        al = Auto.objects.all()
        ctx = {'make_count': mc, 'auto_list': al}
        return render(request, 'autos/auto_list.html', ctx)

class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'autos/make_list.html', ctx)

# I created three classes using CreateView, etc.
class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    template_name = 'autos/make_form.html'
    success_url = reverse_lazy('autos:all')
class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    template_name = 'autos/make_form.html'   
    success_url = reverse_lazy('autos:all')
class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    template_name = 'autos/make_confirm_delete.html'
    success_url = reverse_lazy('autos:all')


# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes
class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')
# We use reverse_lazy rather than reverse in the class attributes
# because views.py is loaded by urls.py and in urls.py as_view() causes
# the constructor for the view class to run before urls.py has been
# completely loaded and urlpatterns has been processed.
# References
# https://docs.djangoproject.com/en/4.2/ref/class-based-views/generic-editing/#createview

