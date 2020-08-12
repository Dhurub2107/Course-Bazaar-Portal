from django.db import models
from django.contrib import admin
class Candidate(models.Model):
    ID=(('CB01','CB01'),('CB02','CB02'),('CB03','CB03'),('CB04','CB04'),('CB05','CB05'),('CB06','CB06'),('CB07','CB07'),('CB08','CB08'))
    CID=models.CharField(max_length=20,unique=True,blank=True,null=True,choices=ID)
    CANDIDATE_NAME=models.CharField(max_length=150)
    COUN = (('INDIA', 'INDIA'), ('US', 'US'), ('DUBAI', 'DUBAI'),('SRI LANKA','SRI LANKA'),('Bangladesh','Bangladesh'))
    COUNTRY=models.CharField(max_length=25,choices=COUN)
    ST=(('UP','UP'),('MP','MP'),('TAMIL_NAADU','TAMIL_NADDU'),('DELHI','DELHI'),('OTHERS','OTHERS'))
    STATE = models.CharField(max_length=20,choices=ST)
    CTY = (('MORADABAD', 'MORADABAD'), ('GHAZIABAD', 'GHAZIABAD'),('MUMBAI','MUMBAI'),('CHENNAI','CHENNAI'),('DELHI','DELHI'),('WASHINGTON','WASHINGTON'),('OTHERS','OTHERS'))
    CITY=models.CharField(max_length=20,choices=CTY)
    PINCODE=models.CharField(max_length=50)
    MAIL_ID=models.EmailField()
    MOBILE1=models.CharField(max_length=50)
    MOBILE2=models.CharField(max_length=50)
    FATHER_NAME=models.CharField(max_length=50)
    COURSES = (('BCA', 'BCA'), ('MCA', 'MCA'), ('B.TECH', 'B.TECH'), ('PHD', 'PHD'), ('MBA', 'MBA'), ('BBA', 'BBA'),('DIPLOMA','DIPLOMA'),('MBBS','MBBS'))
    COURSES_INTERESTED = models.CharField(max_length=50, choices=COURSES,default='OTHERS')
    PLOC = (('MORADABAD', 'MORADABAD'), ('GHAZIABAD', 'GHAZIABAD'), ('MUMBAI', 'MUMBAI'), ('CHENNAI', 'CHENNAI'),
            ('DELHI', 'DELHI'), ('WASHINGTON', 'WASHINGTON'), ('OTHERS', 'OTHERS'))
    PREFFERED_LOCATION=models.CharField(max_length=30,choices=PLOC,default='OTHERS')
class CANDIDATEADMIN(admin.ModelAdmin):
    list_display = ('CID','CANDIDATE_NAME','COUNTRY','CITY','STATE','PINCODE',
    'MAIL_ID','MOBILE1',
    'MOBILE2','FATHER_NAME','COURSES_INTERESTED','PREFFERED_LOCATION')
    list_filter = ('CID', 'CANDIDATE_NAME','COURSES_INTERESTED','CITY')
    search_fields = ('CID', 'CANDIDATE_NAME','COURSES_INTERESTED')

def __str__(self):
    return self.CID+" _ "+self.NAME
