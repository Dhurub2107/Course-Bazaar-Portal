from django.db import models

# Create your models here.

class FeeStructure(models.Model):
    TUTION_FEE=models.PositiveIntegerField()
    EXAM_FEE = models.PositiveIntegerField()
    HOSTEL_FEE = models.PositiveIntegerField()
    BUS_FEE = models.PositiveIntegerField()
    EXTRA_FEE = models.PositiveIntegerField()


    def __int__(self):
        return self.TUTION_FEE