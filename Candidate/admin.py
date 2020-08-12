from django.contrib import admin
from .models import Candidate,CANDIDATEADMIN
from Candidate.models import Candidate
# Register your models here.
admin.site.register(Candidate,CANDIDATEADMIN)
