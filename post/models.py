from django.db import models
from account.models import User


class Post(models.Model): 
    id = models.AutoField(primary_key=True, null=False, blank=False)
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=2000, null=True)
    theater = models.IntegerField(null=True) #fk로 수정 필요
    seat_number = models.IntegerField(null=True) #fk로 수정 필요
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    rate = models.FloatField()

    def __str__(self):
        return self.title
