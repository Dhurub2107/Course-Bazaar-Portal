from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import COLLEGE
# Create your views here.
class CollegeShow(generic.ListView):
    #data=None
    context_object_name = 'College_List'
    template_name = 'ShowCollege.html'
    def get_queryset(self):
        data=COLLEGE.objects.all()
        return data
def CLGShow(request,course_id):
    context_object_name = 'College_List'
    template_name = 'ShowCollege.html'
    data=get_object_or_404(COLLEGE,pk=course_id)
    return render(request,'College.html',{'data':data})
def clgshow(request):
    data = get_object_or_404(COLLEGE)
    return render(request, 'College.html', {'data': data})
