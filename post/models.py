from django.db import models
from userAccount.models import User
from theater.models import Theater
from seat.models import Seat


class Post(models.Model): 
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user_id = models.ForeignKey(User, null=False, blank=True, on_delete=models.CASCADE)
    #user_id = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=2000, null=True)
    #theaterID = models.ForeignKey(Theater, null=False, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, null=False, on_delete=models.CASCADE)
    seatX = models.CharField(max_length=5, null=True)
    seatY = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    rate = models.FloatField(null=True)

    def __str__(self):
        return self.title
