import datetime
from django.core.exceptions import ValidationError
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.static import serve
from django.urls import reverse
import hashlib
import os, csv
from numpy import genfromtxt

from honeypeartea.forms import SchoolPredict, AdmissionChance, HistoryAdmission
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def requirement(request):
    return render(request, 'requirement.html')

def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request, 'contact.html')

class school_predict(TemplateView):
    templatename = 'prediction.html'

    def get(self, request):
        form = SchoolPredict()
        return render(request, self.templatename, {'form': form})

    def post(self, request):
        form = SchoolPredict(request.POST)
        if form.is_valid():
            schoolrank = form.cleaned_data['schoolrank']
            gpa = form.cleaned_data['gpa']
            race = form.cleaned_data['race']
            sat = form.cleaned_data['sat']
            ap = form.cleaned_data['ap']

            # Main decision conditions
            if gpa >= 3 and schoolrank == 'top_30':
                print(f' === You will get in UCLA!!!! ===')
                result = 'UCLA'
            else:
                print('=== you are fucked ===')
                result = 'Stanford'

        args = {'form': form, 'result': result}
        return render(request, self.templatename, args)

class admission_chance(TemplateView):
    templatename = 'chance.html'

    def get(self, request):
        form = AdmissionChance()
        return render(request, self.templatename, {'form': form})

    def post(self, request):
        form = AdmissionChance(request.POST)
        if form.is_valid():
            schoolrank = form.cleaned_data['schoolrank']
            gpa = form.cleaned_data['gpa']
            race = form.cleaned_data['race']
            sat = form.cleaned_data['sat']
            ap = form.cleaned_data['ap']
            college = form.cleaned_data['college']

            # Main decision conditions
            if gpa >= 3 and schoolrank == 'top_30' and college == 'Los Angeles':
                print(f' === You will get in UCLA!!!! ===')
                result = 0.7
            else:
                print('=== you are fucked ===')
                result = 0.1

        args = {'form': form, 'result': result}
        return render(request, self.templatename, args)

class history_admission(TemplateView):
    templatename = 'history.html'

    def get(self, request):
        form = HistoryAdmission()
        return render(request, self. templatename, {'form': form})

    def post(self, request):
        form = HistoryAdmission(request.POST)
        if form.is_valid():
            college = form.cleaned_data['college']
            year = form.cleaned_data['year']
            category = form.cleaned_data['category']

            # CSV file path
            race_matrix = genfromtxt('../static/race.csv', delimiter=',')
            print(race_matrix)

            # Check the result based on the searching category
            if category == 'gpa':
                pass
            elif category == 'sat':
                pass
            elif category == 'race':
                pass
            else:
                print(' == Something is wrong ==')


        args = {'form': form, 'result': result}
        return render(request, self.templatename, args)
