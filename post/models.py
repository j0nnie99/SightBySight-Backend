from django.db import models
from account.models import User
from theater.models import Theater
from seat.models import Seat


class Post(models.Model): 
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user_id = models.ForeignKey(User, null=False, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=2000, null=True)
    theater = models.ForeignKey(Theater, null=False, on_delete=models.CASCADE)
    seat_number = models.ForeignKey(Seat, null=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    rate = models.FloatField()

    def __str__(self):
        return self.title
