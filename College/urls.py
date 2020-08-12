from django.conf.urls import url,include
from django.urls import path
from . import views
urlpatterns = [
    #url(r'^$', views.Show.as_view(), name='Show'),
    url('ShowCollege.html' ,views.CollegeShow.as_view(),name='CollegeShow'),
    path('ShowCollege.html',views.CLGShow,name='CLGShow'),
    url('ShowCollege.html' ,views.CLGShow,name='CLGShow'),
    url('College.html',views.clgshow,name='clgshow'),
    #path('<int:COLLEGE_NAME>',views.CLGShow,name='CLGShow'),
    #url('base.html', views.base, name='base')
    ]