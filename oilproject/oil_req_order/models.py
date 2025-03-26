from django.db import models

# Create your models here.
class Oil_req_order(models.Model):
    plate_name = models.CharField(max_length=20)
    driver_name = models.CharField(max_length=50)
    oil_type = models.CharField(max_length=20)
    oil_amount = models.FloatField()
    oil_per_amount = models.FloatField()
    sup_oil_name = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    emp_money = models.IntegerField()
    
    def __str__(self):
        return self.driver_name+" ทะเบียน "+self.plate_name