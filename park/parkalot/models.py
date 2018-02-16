from django.db import models


# Create your models here.
class slot(models.Model):
    slotname = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    maps = models.CharField(max_length=500,default="https://www.google.com/maps/search/?api=1&query=srm+university")
    def __str__(self):
        return "%s %r" %(self.slotname,self.status)


class user(models.Model):
    carnum = models.CharField(max_length=10)
    star_time = models.DateTimeField('start_time')
    Four_Wheeler = models.BooleanField(default=False)
    Two_Wheeler = models.BooleanField(default=False)
    parkspace = models.ForeignKey(slot, on_delete=models.CASCADE)

    def __str__(self):
        return self.carnum
