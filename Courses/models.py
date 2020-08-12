from django.db import models
from django.contrib import admin
class COURSE(models.Model):
    COURSES = (('BCA', 'BCA'), ('MCA', 'MCA'), ('B.TECH', 'B.TECH'), ('PHD', 'PHD'), ('MBA', 'MBA'), ('BBA', 'BBA'))
    COURSES=models.CharField(max_length=20,choices=COURSES,default='OTHERS')
    POSTED_BY=(('admin','ADMIN'),('college','COLLEGE'))
    POSTEDBY=models.CharField(max_length=150,choices=POSTED_BY)
    NAME = (('TMU', 'TEERTHANKER MAHAVEER UNIVERSITY'), ('AKG', 'AJY KUMAR GARG'), ('MJPRU', 'MJPRU'), ('ABES', 'ABES'))
    COLLEGE_NAME=models.CharField(max_length=25,choices=NAME,)
    LOCATION = (('PAAKWADA', 'PAAKWADA'), ('LOHIA NAGAR', 'LOHIA NAGAR'), ('NEW BUSSTAND', 'NEW BUSSTAND'))
    LOCATION = models.CharField(max_length=50, choices=LOCATION)
    MINQ=(('10+2','10+2'),('UG','UG'),('PG','PG'))
    MINIMUM_QUCALIFICATION=models.CharField(max_length=20,choices=MINQ)
    ELEGIBILITY=(('60-65%','60-65%'),('OTHERS','OTHERS'))
    ELEGIBILITY=models.CharField(max_length=20)
    FEESRANGE=(('2L-3L','2L-3L'),('3L-4L','3L-4L'),('4L-5L','4L-5L'),('5L<','5L<'))
    FEES_RANGE=models.CharField(max_length=50,choices=FEESRANGE)
    CONTACT_PERSON=models.CharField(max_length=20)
    CONTACT_PERSON_MOBILE=models.IntegerField()
    COLLEGE_WEBSITE=models.URLField(max_length=50)
    PLACEMENT = (('50-60', '50-60%'), ('60-70', '60-70%'), ('70-80', '70-80%'), ('80-90', '80-90%'), ('90-100', '90-100%'))
    PLACEMENT = models.CharField(max_length=20, choices=PLACEMENT)
    LASTDATE=models.DateField()
    CURRENTSTATUS=models.CharField(max_length=50)



class COURSEADMIN(admin.ModelAdmin):
    list_display = ('COURSES', 'POSTEDBY', 'COLLEGE_NAME', 'LOCATION','MINIMUM_QUCALIFICATION', 'ELEGIBILITY',
                    'FEES_RANGE', 'CONTACT_PERSON', 'CONTACT_PERSON_MOBILE',
                    'PLACEMENT', 'LASTDATE', 'CURRENTSTATUS')
    search_fields = ('COURSES', 'COLLEGE_NAME', 'FEES_RANGE')
    list_filter = ('COLLEGE_NAME', 'COURSES', 'FEES_RANGE', 'LOCATION')
def __str__(self):
    return self.COLLEGE_NAME

