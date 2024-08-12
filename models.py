from django.db import models

#whatever changes or additions to the models.py file must run migrations
# Create your models here.
class EmployeeDB(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    id = models.CharField(max_length=50,primary_key=True, blank=False, null=False)
    status = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
# class VehiclesDB(models.Model):
#     number = models.IntegerField(primary_key=True, blank=False, null=False)
#     moldelNumber = models.CharField(max_length=50, blank=False, null=False)
#     ChasisNumber = models.CharField(max_length=50)
#     RegistrationNumber = models.CharField(max_length=50)
#     Mileage = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.number
