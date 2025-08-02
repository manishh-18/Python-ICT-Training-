from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)



class PollResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100)

