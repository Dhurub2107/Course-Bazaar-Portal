from django.contrib import admin
from .models import College
admin.site.register(College)
admin.site.site_header = 'COURSE BAZAAR ADMIN'