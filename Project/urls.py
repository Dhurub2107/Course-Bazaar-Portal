from django.conf.urls import url,include

from . import views

urlpatterns = [
    url('index.html', views.index, name='index'),

    url('about.html', views.about, name='about'),

    url('codes.html', views.codes, name='codes'),

    url('contact.html', views.contact, name='contact'),

    url('icons.html', views.icons, name='icons'),

    url('gallery.html', views.gallery, name='gallery'),

    #url('ShowCandidate.html' ,views.Show ,name='Show'),

    url('signup.html',views.signup,name='signup'),
    url('Otp.html',views.Otp,name='Otp'),
    url('login.html', views.login, name='login'),

]
