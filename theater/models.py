from django.db import models

# Create your models here.
class Theater(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=250, null=True)
    contact = models.CharField(max_length=100, null=True)
    info = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name