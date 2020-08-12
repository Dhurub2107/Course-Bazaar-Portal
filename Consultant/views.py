from django.shortcuts import render
from django.views import generic
from django.views.generic import DetailView
from django.views.generic import View
from .models import Consultant
# Create your views here.
class ConShow(generic.ListView):
    #data=None
    context_object_name = 'Consultant_List'
    template_name = 'ShowConsultant.html'
    def get_queryset(self):
        data=Consultant.objects.all()
        return data
class homeShow(generic.ListView):
    def home(request):
        query = request.GET.get('ID')
        message = format(query)
        template = "ShowConsultant.html"
        data = Consultant.objects.get(ID='CD03')
        return render(request, template, data)
'''class Showdata(generic.ListView):
    context_object_name = 'Consultant_List'
    template_name = "ShowConsultant.html"
    def get_queryset(self):
        data=Consultant.objects.all()
        return data'''



