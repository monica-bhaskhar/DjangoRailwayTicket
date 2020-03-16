from django.db import models

# Create your models here.
class BookTicket(models.Model):

    
    GENDER_CHOICES = (('Male', 'Male'),('Female', 'Female'),)
    BERTH_CHOICES = (('Upper', 'Upper'),('Lower', 'Lower'),('Middel', 'Middel'),('Side', 'Side'))
    STATUS_CHOICES = (('Confirmed', 'Confirmed'),('RAC ', 'RAC'),('Waiting', 'Waiting'))
    COACH_CHOICES = (('S1', 'S1'),('S2', 'S2'),('S3', 'S3'),('S4', 'S4'))


    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length = 6, choices = GENDER_CHOICES)
    berth_preference = models.CharField(max_length = 10, choices = BERTH_CHOICES)
    coach = models.CharField(max_length = 10, choices = COACH_CHOICES)
    status = models.CharField(max_length = 10, choices = STATUS_CHOICES)


    def __str__(self):
        return self.name
