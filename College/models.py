from django.db import models
from django.contrib import admin
class COLLEGE(models.Model):
    NAME=(('TMU','TEERTHANKER MAHAVEER UNIVERSITY'),('AKG','AJY KUMAR GARG'),('MJPRU','MJPRU'),('ABES','ABES'),('SUN','SUNDERDEEP ENGINERRING COLLEGE'))
    COLLEGE_NAME=models.CharField(choices=NAME,max_length=150)
    COUNTRY = (('INDIA','INDIA'),('US','US'),('DUBAI','DUBAI'))
    COUNTRY = models.CharField(max_length=50, choices=COUNTRY)
    STATE=(('UP','UP'),('MP','MP'))
    STATE = models.CharField(max_length=50,choices=STATE)
    CITY=(('MORADABAD','MORADABAD'),('GHAZIABAD','GHAZIABAD'))
    CITY=models.CharField(max_length=50,choices=CITY)
    LOCATION=(('PAAKWADA','PAAKWADA'),('LOHIA NAGAR','LOHIA NAGAR'),('NEW BUSSTAND','NEW BUSSTAND'))
    LOCATION=models.CharField(max_length=50,choices=LOCATION)
    PINCODE=models.IntegerField()
    LANDLINE_NUMBER=models.IntegerField()
    COLLEGE_MOBILE=models.IntegerField()
    MAIL_ID=models.EmailField()
    PASSWORD=models.IntegerField()
    COURSES=(('BCA','BCA'),('MCA','MCA'),('B.TECH','B.TECH'),('PHD','PHD'),('MBA','MBA'),('BBA','BBA'))
    COURSES=models.CharField(max_length=50,choices=COURSES)
    CONTACT_PERSON_NAME=models.CharField(max_length=50)
    CONTACT_PERSON_MOBILE=models.IntegerField()
    UNIVERSITY=(('TMU','TMU'),('AKTU','AKTU'),('MJPRU','MJPRU'))
    UNIVERSITY=models.CharField(max_length=50,choices=UNIVERSITY)
    PLACEMENT=(('50-60','50-60%'),('60-70','60-70%'),('70-80','70-80%'),('80-90','80-90%'),('90-100','90-100%'))
    PLACEMENT = models.CharField(max_length=20,choices=PLACEMENT)
    RATING=(('3.0','3.0'),('3.5','3.5'),('4.0','4.0'),('4.5','4.5'),('4.7','4.7'),('5.0','5.0'))
    RATING=models.CharField(max_length=50,choices=RATING)
    HOSTEL=(('Y','YES'),('N','NO'))
    HOSTEL=models.CharField(max_length=50,choices=HOSTEL)
    COLLEGE_WEBSITE=models.URLField(max_length=50)
    COLLEGE_GALLERY=models.ImageField()
class COLLEGEADMIN(admin.ModelAdmin):
    list_display = ('COLLEGE_NAME','COUNTRY','STATE','CITY','LOCATION','PINCODE','LANDLINE_NUMBER',
    'COLLEGE_MOBILE','MAIL_ID','COURSES',
    'CONTACT_PERSON_NAME','CONTACT_PERSON_MOBILE','UNIVERSITY','PLACEMENT','RATING',
    'HOSTEL','COLLEGE_WEBSITE','COLLEGE_GALLERY')
    list_filter = ('COLLEGE_NAME', 'COURSES','UNIVERSITY','CITY')
    search_fields = ('COLLEGE_NAME', 'COURSES','CITY')


def __str__(self):
        return self.COLLEGE_NAME+'__'+self.MAIL_ID