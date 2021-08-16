from django.db import models

# Create your models here.
class ScrapFriend(models.Model):
    nickname = models.CharField(max_length=100, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    likes = models.CharField(max_length=250)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    living = models.CharField(max_length=150, null=True, blank=True)


    def __str__(self):
        return str(self.nickname)
