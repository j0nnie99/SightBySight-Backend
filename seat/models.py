from django.db import models
from theater.models import Theater


# Create your models here.
class Seat(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    theater_id = models.ForeignKey(Theater, null=True, blank=True, on_delete=models.CASCADE)
    locX = models.CharField(max_length=5, null=False)
    locY = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.locX