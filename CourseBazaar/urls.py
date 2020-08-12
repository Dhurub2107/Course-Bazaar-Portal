from django.contrib import admin
from django.conf.urls import url,include

urlpatterns = [
    url('Project/', include('Project.urls')),
    url('Candidate/',include('Candidate.urls')),
    url('College/',include('College.urls')),
    url('Consultant/',include('Consultant.urls')),
    url('Courses/',include('Courses.urls')),
    url('admin/', admin.site.urls),
]
