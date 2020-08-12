from django.http import HttpResponse
from django.template import loader
#My Work
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect,HttpResponse
from django.views import generic

def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())


def about(request):
    template=loader.get_template('about.html')
    return HttpResponse(template.render())


def codes(request):
    template=loader.get_template('codes.html')
    return HttpResponse(template.render())

def contact(request):
    template=loader.get_template('contact.html')
    return HttpResponse(template.render())

def gallery(request):
    template=loader.get_template('gallery.html')
    return HttpResponse(template.render())
def mps(request):
    template=loader.get_template('google-mps.html')
    return HttpResponse(template.render())

def login(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())
def icons(request):
    template=loader.get_template('icons.html')
    return HttpResponse(template.render())

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            Email = form.cleaned_data.get('Email')
            raw_password = form.cleaned_data.get('password')

            user = authenticate(username=Email, password=raw_password)
            login(request, user)
            return render(request,'index.html',{'form:':form})
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
class Otp(generic.ListView):
    #data=None
    template_name = 'Otp.html.html'
    def get_queryset(self):
        template = loader.get_template('Otp.html')
        return HttpResponse(template.render())
