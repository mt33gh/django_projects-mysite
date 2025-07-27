from django.shortcuts import render
# Create your views here.
from gview.models import Cat, Dog, Horse, Car
from django.views import View, generic

class CatListView(View):
    def get(self, request) :
        stuff = Cat.objects.all()
        cntx = { 'cat_list': stuff }
        return render(request, 'gview/cat_list.html', cntx)
class CatDetailView(View):
    def get(self, request, pk_from_url) :
        obj = Cat.objects.get(pk=pk_from_url)
        cntx = { 'cat': obj }
        return render(request, 'gview/cat_detail.html', cntx)

class DogListView(View):
    model = Dog
    def get(self, request) :
        modelname = self.model._meta.verbose_name.title().lower()
        stuff = self.model.objects.all()
        cntx = { modelname+'_list': stuff }
        return render(request, 'gview/'+modelname+'_list.html', cntx)
class DogDetailView(View):
    model = Dog
    def get(self, request, pk) :
        modelname = self.model._meta.verbose_name.title().lower()
        obj = self.model.objects.get(pk=pk)
        cntx = { modelname : obj }
        return render(request, 'gview/'+modelname+'_detail.html', cntx)

class HorseListView(generic.ListView):
    model = Horse
class HorseDetailView(generic.DetailView):
    model = Horse

# Lets review how inheritance works to avoid repeating ourselves
# It is all about convention
class DJ4EListView(View):
    def get(self, request) :
        modelname = self.model._meta.verbose_name.title().lower()
        stuff = self.model.objects.all()
        cntx = { modelname+'_list': stuff }
        return render(request, 'gview/'+modelname+'_list.html', cntx)
class DJ4EDetailView(View):
    def get(self, request, pk) :
        modelname = self.model._meta.verbose_name.title().lower()
        obj = self.model.objects.get(pk=pk)
        cntx = { modelname : obj }
        return render(request, 'gview/'+modelname+'_detail.html', cntx)
# Lets reuse those "generic" classes
class CarListView(DJ4EListView):
    model = Car
class CarDetailView(DJ4EDetailView):
    model = Car

# Lets explore how (badly) we can override some of what goes on...
class WackyEquinesView(generic.ListView):
    model = Car
    template_name = 'gview/wacky.html'  # Convention: gview/car_list.html
    def get_queryset(self, **kwargs):
        crazy = Horse.objects.all()    # Convention: Car
        print('CRAZY')
        return crazy
    # Add something to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['crazy_thing'] = 'CRAZY THING'
        return context


