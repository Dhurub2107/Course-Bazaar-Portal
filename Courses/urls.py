from django.conf.urls import url,include
from django.urls import path
from Courses import views
urlpatterns = [
    #url(r'^$', views.Show.as_view(), name='Show'),
    url('ShowCourse.html' ,views.CourseShow.as_view(),name='CourseShow'),
    url('ShowCourse.html' ,views.Course,name='Course'),
    url('course.html',views.course,name='course'),
    path('<int:course_id>',views.Course,name='Course'),
    ]