from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from form.forms import BasicForm #, CatForm
from form.models import Cat, Vehicle
import html

def example(request) :
    form = BasicForm()
    return HttpResponse(form.as_table())

# Call as dumpdata('GET', request.GET)
def dumpdata(place, data) :
    retval = ""
    if len(data) > 0 :
        retval += '<p>Incoming '+place+' data:<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval

class DumpPostView(View):  # modified 
    def post(self, request) :
        form = BasicForm(request.POST)
        if form.is_valid():
        # Form is good → dump the cleaned data
            dump = dumpdata('POST', request.POST)
            ctx = {'title': 'request.POST', 'dump': dump}
            return render(request, 'form/dump.html', ctx)
        else:
        # Form has errors → show form again with error messages  
            ctx = {'form' : form}      
            return render(request, 'form/form.html', ctx)

class SimpleCreate(DumpPostView): 
    def get(self, request) :
        form = BasicForm()
        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)

class SimpleUpdate2(DumpPostView):
    def get(self, request) :
        # Get a Vehicle object from the database. Use any ID you want (e.g. 1 here)
        vehicle = Vehicle.objects.first()
        if vehicle is None:
            return HttpResponse("No vehicles in the database.")
        # Initialize the form with data from the model instance
        form = BasicForm(initial={
            'title': vehicle.title,
            'mileage': vehicle.mileage,
            'purchase_date': vehicle.purchase_date,
        })
        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)

class SimpleUpdate(DumpPostView):
    def get(self, request) :
        old_data = {
            'title': 'SakaiCar', 
            'mileage' : 42, 
            'purchase_date': '2018-08-14'
        }
        form = BasicForm(old_data)
        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)

class Validate(DumpPostView):
    def get(self, request) :
        old_data = {
            'title': 'SakaiCar', 
            'mileage' : 42, 
            'purchase_date': '2018-08-14'
        }
        form = BasicForm(initial=old_data)
        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)
    def post(self, request) :
        form = BasicForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, 'form/form.html', ctx)
        # If there are no errors, we would save the data
        x = reverse('form:success')
        return redirect(x)

def success(request) :
    return HttpResponse('Thank you!')
