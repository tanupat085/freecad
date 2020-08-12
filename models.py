from django.db import models



class UpdateProgress(models.Model) :
    obj_code = models.CharField(max_length=100 , verbose_name= ' work serial in freecad')
    obj_name = models.CharField(max_length=100 , verbose_name= 'name of work want to follow')
    obj_progress = models.IntegerField()

    def __str__(self):
        return self.obj_code 





# Create your models here.
