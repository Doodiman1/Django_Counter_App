from django.db import models

# Create your models here.

class Visit(models.Model):
    userid = models.IntegerField(primary_key = True, default=0)
    username = models.CharField(max_length = 20, default = "Guest")
    count = models.IntegerField()
    def __str__(self):
        return self.username
    def __int__(self):
        return self.count


