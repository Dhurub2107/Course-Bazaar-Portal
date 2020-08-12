from django.shortcuts import render
from django.views import generic
from .models import COURSE
from django.shortcuts import render,get_object_or_404
# Create your views here.
class CourseShow(generic.ListView):
    #data=None
    context_object_name = 'Course_List'
    template_name = 'ShowCourse.html'
    def get_queryset(self):
        data=COURSE.objects.all()
        return data
def Course(request,course_id):
    data=get_object_or_404(COURSE,pk=course_id)
    return render(request,'Course.html',{'data':data})
def course(request):
    data = get_object_or_404(COURSE)
    return render(request, 'Course.html', {'data': data})