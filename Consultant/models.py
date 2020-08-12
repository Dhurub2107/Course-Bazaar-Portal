from django.db import models
from django.contrib import admin
# Create your models here.
class Consultant(models.Model):
    CANID = (('CD01', 'CD01'), ('CD02', 'CD02'), ('CD03', 'CD03'), ('CD04', 'CD04'), ('CD05', 'CD05'), ('CD06', 'CD06'),
           ('CD07', 'CD07'), ('CD08', 'CD08'),('CD09', 'CD09'),('CD10', 'CD10'))
    ID=models.CharField(max_length=10,primary_key=True,choices=CANID)
    NAME=models.CharField(max_length=20,default='XYZ')
    COUNTRY = (
    ('INDIA', 'INDIA'), ('US', 'US'), ('DUBAI', 'DUBAI'), ('SRI LANKA', 'SRI LANKA'), ('Bangladesh', 'Bangladesh'))
    COUNTRY = models.CharField(max_length=25, choices=COUNTRY)
    STATE = (('UP', 'UP'), ('MP', 'MP'), ('TAMIL_NAADU', 'TAMIL_NADDU'), ('DELHI', 'DELHI'), ('OTHERS', 'OTHERS'))
    STATE = models.CharField(max_length=20, choices=STATE)
    CITY = (('MORADABAD', 'MORADABAD'), ('GHAZIABAD', 'GHAZIABAD'), ('MUMBAI', 'MUMBAI'), ('CHENNAI', 'CHENNAI'),
            ('DELHI', 'DELHI'), ('WASHINGTON', 'WASHINGTON'), ('OTHERS', 'OTHERS'))
    CITY = models.CharField(max_length=20, choices=CITY)
    PINCODE = models.PositiveIntegerField()
    MAIL_ID = models.EmailField()
    MOBILE1 = models.PositiveIntegerField()
    MOBILE2 = models.PositiveIntegerField()

class CONSULTANTADMIN(admin.ModelAdmin):
    list_display = ('ID', 'NAME', 'COUNTRY','STATE', 'CITY', 'PINCODE',
                    'MAIL_ID', 'MOBILE1',
                    'MOBILE2')
    list_filter = ('ID', 'NAME', 'CITY')
    search_fields = ('ID', 'NAME', 'CITY')

def __str__(self):
    return self.CID

