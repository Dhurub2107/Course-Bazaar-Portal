from django.conf.urls import url,include
from Candidate import views
urlpatterns = [
    #url(r'^$', views.Show.as_view(), name='Show'),
    url('ShowCandidate.html' ,views.Show.as_view(),name='Show'),

]