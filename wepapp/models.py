from django.db import models

# Create your models here.
class employees(models.Model):
    firstname = models.CharField(max_length =30)
    lastname = models.CharField(max_length =30)
    emp_id = models.IntegerField()
    phone_number = models.CharField(max_length=14, blank=True)


    def _str_(self):
     return self.firstname