from django.db import models

class Placement(models.Model):

    COLLEGENAME=models.CharField(max_length=20)
    COMPANYNAME=models.CharField(max_length=150)
    COURSE=models.CharField(max_length=25)
    NOOFPERSON=models.IntegerField()
    PACKAGE=models.PositiveIntegerField()
    LOCATION=models.CharField(max_length=20)

    def __str__(self):
        return self.COLLEGENAME+" "+self.COMPANYNAME
