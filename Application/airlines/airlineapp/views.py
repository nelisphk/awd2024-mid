from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic import DeleteView, UpdateView
from .models import *
from .forms import *

## VIEWS HAVE NOT BEEN IMPLEMENTED TO TEMPLATES FOR THE MIDTERM AS ONLY REST END POINTS SPECIFIED

class AirlineList(ListView):
    model = Airlines
    context_object_name = 'airlines'
    template_name = 'airlineapp/index.html'

class AirlineInfo(DetailView):
    model = Airlines
    context_object_name = 'airline'
    template_name = 'airlineapp/airline_info.html'

class AirportInfo(DetailView):
    model = Airports
    context_object_name = 'airport'
    template_name = 'airlineapp/airport_info.html'

class AirlineCreate(CreateView):
    model = Airlines
    template_name = 'airlineapp/create_airline.html'
    form_class = AirlineForm
    success_url = '/'

class AirlineUpdate(UpdateView):
    model = Airlines
    fields = ['name', 'alias', 'iata', 'icao', 'callsign', 'active', 'country']
    template_name_suffix = '_update_form'
    success_url = '/'

class AirlineDelete(DeleteView):
    model = Airlines
    success_url = '/'