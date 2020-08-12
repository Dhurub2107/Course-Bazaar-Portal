from django.conf.urls import url,include
from Consultant import views
urlpatterns = [
    #url(r'^$', views.Show.as_view(), name='Show'),
    url('ShowConsultant.html' ,views.ConShow.as_view(),name='ConShow'),
    url('ShowConsultant.html',views.homeShow.as_view(),name='homeShow'),
    ]