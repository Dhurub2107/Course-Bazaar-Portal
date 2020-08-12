from django.template import loader
#########################
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect,HttpResponse
from .models import Candidate
from django.views.generic import TemplateView,ListView
from django.views import generic
from Candidate.forms import CandidateForm
data = Candidate()
data.save()
form = CandidateForm()

class Show(generic.ListView):
    #data=None
    context_object_name = 'Candidate_list'
    template_name = 'ShowCandidate.html'
    def get_queryset(self):
        data = Candidate.objects.exclude(CID='cb02')
        #data=Candidate.objects.all()
        return data
def myshow(self):
    context_object_name = 'Candidate_list'
    template_name = 'ShowCandidate.html'
    data1=Candidate.objects.exclude(CID='cb02')
    return data1